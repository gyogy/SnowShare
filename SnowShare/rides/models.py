from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=20)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    pw = models.CharField(max_length=40)


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
    capacity = models.IntegerField
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Resort(models.Model):
    name = models.CharField(max_length=40)


class Ride(models.Model):
    destination = models.ForeignKey(Resort, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)