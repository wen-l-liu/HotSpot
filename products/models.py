from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Brand(models.Model):
    """ Brand model """
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Product model """
    name = models.CharField(max_length=254)
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
