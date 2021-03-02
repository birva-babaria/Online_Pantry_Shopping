from django.db import models

# Create your models here.

class customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)
