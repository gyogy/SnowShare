from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Car, Ride, PassengerRide


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


class TakeRide(forms.ModelForm):
    class Meta:
        model = PassengerRide
        exclude = ('ride', 'passanger')
    
    def save(self, psg=None, ride=None, commit=True):
        pass_ride = super(TakeRide, self).save(commit=False)
        pass_ride.passenger = psg
        pass_ride.ride = ride
        if commit:
            pass_ride.save()
        return pass_ride
