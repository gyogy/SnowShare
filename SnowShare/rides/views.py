from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, CreateCar, CreateRide, TakeRide
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Car, Ride, Resort, User


@login_required(login_url='login')
def index(request):
    cars = Car.objects.filter(owner__username=request.user.username)
    context = {"cars": cars}
    return render(request, 'accounts/index.html', context)


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
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def new_car(request):

    if request.method == "POST":
        data = request.POST
        form = CreateCar(data=data)
        if form.is_valid():
            new_car = form.save(user=request.user)
            return render(request, 'cars/car_detail.html', {'new_car': new_car})
        else:
            return render(request, 'cars/add_car.html', {'form': form})
    else:
        form = CreateCar()
        return render(request, 'cars/add_car.html', {'form': form})


@login_required(login_url='login')
def delete_car(request, car_id):
    if request.method == 'POST':
        Car.objects.filter(id=car_id).delete()
    return redirect('index')


@login_required(login_url='login')
def new_ride(request):
    cars = Car.objects.filter(owner__username=request.user.username)
    if request.method == "POST":
        data = request.POST
        form = CreateRide(data=data)
        form.fields["car"].queryset = cars
        if form.is_valid():
            ride = form.save(driver=request.user)
            return render(request, 'rides/detail.html', {'ride': ride})
        else:
            return render(request, 'rides/add.html', {'form': form})
    else:
        form = CreateRide()
        form.fields["car"].queryset = cars
        return render(request, 'rides/add.html', {'form': form})


@login_required(login_url='login')
def listRides(request):
    rides = Ride.objects.all()
    return render(request, 'rides/list.html', {'rides': rides})


@login_required(login_url='login')
def view(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    passangers = User.objects.filter(passengerride__ride_id=ride_id)
    names = [passanger.username for passanger in passangers]
    return render(request, 'rides/detail.html', {'ride': ride, 'names': names})


@login_required(login_url='login')
def take_ride(request):
    if request.method == "POST":
        data = request.POST
        ride = Ride.objects.get(id=data['ride_id'])
        form = TakeRide()
        if ride.free_seats <= 0:
            messages.info(request, 'All seats are already taken. Sorry. :(')
            return redirect('resorts')
        else:
            ride.free_seats -= 1
            ride.save()
            form.save(psg=request.user, ride=ride)
            # return redirect('resorts')
            return redirect('view', ride.id)
    else:
        form = TakeRide()
        return redirect('resorts')


@login_required(login_url='login')
def list_resorts(request):
    resorts = Resort.objects.all()
    return render(request, 'resorts/list.html', {'resorts': resorts})


@login_required(login_url='login')
def resort_details(request, resort_id):
    resort = get_object_or_404(Resort, id=resort_id)
    rides = Ride.objects.filter(destination=resort_id)
    return render(request, 'resorts/detail.html', {'resort': resort, 'rides': rides})


@login_required(login_url='login')
def driver(request):
    user_id = request.user
    name = request.user.username
    rides = Ride.objects.filter(driver=user_id)
    return render(request, 'rides/driver.html', {'rides': rides, 'name': name})


@login_required(login_url='login')
def passanger(request):
    user_id = request.user
    name = request.user.username
    rides = Ride.objects.filter(passengerride__passenger=user_id)
    return render(request, 'rides/passanger.html', {'rides': rides, 'name': name})
