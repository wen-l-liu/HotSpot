from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from cloudinary.models import CloudinaryField
# Create your models here.


class Brand(models.Model):
    """ Brand model """
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Product model """
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    image = CloudinaryField('image', default='placeholder')
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def update_rating(self):
        """Calculate and update the average rating from reviews"""
        avg_rating = self.reviews.filter(approved=True).aggregate(Avg('rating'))['rating__avg']
        self.rating = round(avg_rating, 1) if avg_rating else None
        self.save()

    def __str__(self):
        return self.name


class Flavour(models.Model):
    """ Flavour model for products """
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE,
        primary_key=True, related_name='flavours')

    heat = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True
    )
    STRENGTH_CHOICES = (
        ('none', 'None'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    fruit = models.CharField(choices=STRENGTH_CHOICES, max_length=10, null=True, blank=True)
    garlic = models.CharField(choices=STRENGTH_CHOICES, max_length=10, null=True, blank=True)
    sweet = models.CharField(choices=STRENGTH_CHOICES, max_length=10, null=True, blank=True)
    smoke = models.CharField(choices=STRENGTH_CHOICES, max_length=10, null=True, blank=True)
    salt = models.CharField(choices=STRENGTH_CHOICES, max_length=10, null=True, blank=True)
    vinegar = models.CharField(choices=STRENGTH_CHOICES, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.product.name


class Review(models.Model):
    """ Review model for products """
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviewer"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5)])
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
        # This means that the most recent comments are shown first.

    def __str__(self):
        return f"Review by {self.author} for {self.product.name}"


@receiver(post_save, sender=Review)
def update_product_rating_on_save(sender, instance, **kwargs):
    """Update product rating when a review is saved"""
    if instance.approved:
        instance.product.update_rating()


@receiver(post_delete, sender=Review)
def update_product_rating_on_delete(sender, instance, **kwargs):
    """Update product rating when a review is deleted"""
    instance.product.update_rating()
