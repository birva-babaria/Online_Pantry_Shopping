from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_ID = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    customer_address = models.TextField()
    customer_email = models.EmailField(max_length=50)
    customer_phone = models.BigIntegerField()

class Login(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=8)

class Product(models.Model):
    product_ID = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    product_desc = models.TextField()
    product_price = models.DecimalField(max_digits=5,decimal_places=2)
    product_img = models.ImageField(upload_to='imgs')
    product_stock = models.IntegerField()

class Cart(models.Model):
    cart_ID = models.AutoField(primary_key=True)
    cart_product_ID = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    cart_customer_ID = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    subtotal = models.DecimalField(max_digits=5,decimal_places=2)
    quantity = models.IntegerField()

class Order(models.Model):
    order_ID = models.AutoField(primary_key=True)
    order_product_ID = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order_customer_ID = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    order_cart_ID = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    order_date = models.DateField()
    delivery_date = models.DateField()

