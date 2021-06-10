from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Address(models.Model):
    postal_code = models.CharField(max_length=10)
    street_name = models.CharField(max_length=255)
    building_number = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.street_name} {self.building_number}, {self.postal_code} {self.city}, {self.city.country}'


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='hotel_pics')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('hotel-detail', kwargs={'pk': self.pk})


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    price = models.FloatField(validators=[MinValueValidator(0)])
    max_people = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.room_type.hotel.name}: {self.room_number}'


class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=None)
    date = models.DateField(auto_now_add=True)
    check_in = models.DateField()
    check_out = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.guest}'


class Reviews(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField()

    def __str__(self):
        return f'{self.guest}: {self.hotel}'
