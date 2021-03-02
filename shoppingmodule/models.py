from django.db import models

# Create your models here.

class product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.CharField(max_length=100)
