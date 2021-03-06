from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import RegexValidator


# class User(models.Model):
#     nickname = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     pw = models.CharField(max_length=40)


class Car(models.Model):
    SEDAN = 'Sed'
    VAN = 'Van'
    PICKUP = 'Pic'
    TRUCK = 'Trk'
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (VAN, 'Van'),
        (PICKUP, 'Pick-up'),
        (TRUCK, 'Truck'),
    ]

    make = models.CharField(max_length=20)
    typ = models.CharField(
        max_length=3,
        choices=CAR_TYPE_CHOICES,
        default=SEDAN,
    )
    capacity = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner.username}\'s {self.make} {self.typ}'


class Resort(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Ride(models.Model):
    destination = models.ForeignKey(Resort, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    startPoint = models.CharField(max_length=15)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^[0-9]*$')])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    free_seats = models.IntegerField()

    def __str__(self):
        return f'A ride to {self.destination} with {self.free_seats} free seats.'


class PassengerRide(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
