from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from shoppingmodule.models import product,shoppingcart
from loginmodule.models import customer

# Create your views here.

def viewhome(request):
    prods = product.objects.all()
    return render(request, 'home.html', {'prods': prods})

def viewaboutus(request):
    return render(request, 'aboutus.html')

def addtocart(request):
    p_id = request.GET['p_id']
    c = shoppingcart(cart_cust_id=customer.objects.get(cust_id = request.session['cust_id']), cart_prod_id=product.objects.get(prod_id = p_id))
    c.save()
    return HttpResponseRedirect('/shoppingmodule/viewcart/')

def viewcart(request):
    prods = shoppingcart.objects.all().filter(cart_cust_id = customer.objects.get(cust_id = request.session['cust_id']))
    return render(request, 'cart.html', {'prods': prods})

