# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return HttpResponse("Hello! You're at the ride sharing index.")


def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
