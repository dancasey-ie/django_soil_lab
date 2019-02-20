from django.db import models
from products.models import Product
from django.conf import settings

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = (('Ordered'),('Ordered')), (('Processed'),('Processed'))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Ordered')
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True) # blank=True, means not required
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()


    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.username)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)