from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator, validate_comma_separated_integer_list

# Create your models here.

def emptyList():
    return list()

class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField (validators=[MinValueValidator(0)], default=0)
    is_discounted = models.BooleanField(default=False)
    discounted_price = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    thumbnail = models.URLField(max_length=1000)
    gallery = ArrayField(
            models.URLField(max_length=1000, blank=False)
    )
    rating = models.DecimalField(
        decimal_places=2,
        max_digits=50,
        default=None, blank=True, null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    available_colors = ArrayField(
            models.CharField(max_length=1000, blank=False)
    )
    available_sizes = ArrayField(
            models.CharField(max_length=1000, blank=False)
    )
    description = models.TextField(max_length=600)

    def __str__(self):
        return self.name
