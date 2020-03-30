from django.db import models
from photos.models import Photo

# Create your models here.
class Order(models.Model):
    """
    Defines data for the order table, including billing details.
    """
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    user_name = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.id, self.date, self.user_name, self.email)


class OrderLineItem(models.Model):
    """
    Handles the data for each line ordered by a user on the above user form.
    """
    order = models.ForeignKey(Order, null=False)
    photo = models.ForeignKey(Photo, null=False)

    def __str__(self):
        return "{0} @ {1}".format(
            self.photo.name, self.photo.price)

