from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateCar
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    return render(request, 'accounts/index.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        context = {"user": request.user}
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                context = {"user": user}
                login(request, user)
                return render(request, 'accounts/index.html', context)
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def new_car(request):
    if request.method == "POST":
        data = request.POST
        form = CreateCar(data=data)
        if form.is_valid():
            new_car = form.save()
            return render(request, 'cars/car_detail.html', {'new_car': new_car})
        else:
            return render(request, 'cars/add_car.html', {'form': form})
    else:
        form = CreateCar()
        return render(request, 'cars/add_car.html', {'form': form})
