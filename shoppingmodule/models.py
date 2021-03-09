from django.db import models
from loginmodule.models import customer
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
# Create your models here.

class product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=100)

class shoppingcart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_prod_id = models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    cart_cust_id = models.ForeignKey(customer,on_delete=models.CASCADE,null=True)

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_cust_id = models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    price = models.FloatField()
    orderdate = models.DateTimeField(default=datetime.now, blank=True)
    deliverdate = models.DateTimeField(default=timezone.now() + timedelta(days=1), blank=True)
    status = models.CharField(max_length = 20, default = "pending")
    

class orderitems(models.Model):
    orderitems_id = models.AutoField(primary_key=True)
    orderitems_order_id = models.ForeignKey(order,on_delete=models.CASCADE,null=True)
    orderitems_prod_id = models.ForeignKey(product,on_delete=models.CASCADE,null=True)