from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.TimeField()

    def __str__(self):
        return self.name
