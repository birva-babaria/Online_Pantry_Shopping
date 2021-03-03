from django.db import models
from loginmodule.models import customer
# Create your models here.

class product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.CharField(max_length=100)

class shoppingcart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_prod_id = models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    cart_cust_id = models.ForeignKey(customer,on_delete=models.CASCADE,null=True)