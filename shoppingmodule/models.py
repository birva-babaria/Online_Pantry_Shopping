from django.db import models

# Create your models here.

class product(models.Model):
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.CharField(max_length=100)
