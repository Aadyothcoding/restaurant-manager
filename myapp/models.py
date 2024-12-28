from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description =models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} {self.time}"