from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    purpose = models.CharField(max_length=254, default='')
    elements_determined = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=254,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    test_type = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name