from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Car, Ride


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class CreateCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'typ', 'capacity')

    def save(self, user=None, commit=True):
        car = super(CreateCar, self).save(commit=False)
        car.owner = user
        if commit:
            car.save()
        return car


class CreateRide(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ('destination', 'date', 'car', 'free_seats', 'price')

    def save(self, driver=None, commit=True):
        ride = super(CreateRide, self).save(commit=False)
        ride.driver = driver
        if commit:
            ride.save()
        return ride
