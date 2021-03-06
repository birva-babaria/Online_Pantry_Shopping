from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from shoppingmodule.models import product,shoppingcart,orderitems,order
from loginmodule.models import customer
import datetime
from django.utils import timezone

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
    price = 0.0
    TAX = 19.05
    for prod in prods:
        price = price + prod.cart_prod_id.price
    subtotal = price + TAX
    return render(request, 'cart.html', {'prods': prods, 'price': price, 'TAX': TAX, 'subtotal': subtotal})

def removefromcart(request):
    c_id = request.GET['c_id']
    prod = shoppingcart.objects.get(cart_id = c_id)
    prod.delete()
    return HttpResponseRedirect('/shoppingmodule/viewcart/')

def buynow(request):
    p_id = request.GET['p_id']
    prod = product.objects.get(prod_id = p_id)
    cust = customer.objects.get(cust_id = request.session['cust_id'])
    price = prod.price
    TAX = 19.05
    subtotal = price + TAX
    context = {
        'prod': prod,
        'cust': cust,
        'TAX': TAX,
        'subtotal': subtotal
    }
    return render(request, 'buynowbill.html', context)

def cartbill(request):
    prods = shoppingcart.objects.all().filter(cart_cust_id = customer.objects.get(cust_id = request.session['cust_id']))
    cust = customer.objects.get(cust_id = request.session['cust_id'])
    price = 0.0
    TAX = 19.05
    for prod in prods:
        price = price + prod.cart_prod_id.price
    subtotal = price + TAX
    context = {
        'prods': prods, 
        'cust' : cust,
        'price': price, 
        'TAX': TAX, 
        'subtotal': subtotal
    }
    return render(request, 'cartbill.html', context)

# def confirmorder(request):
#     o = order(order_cust_id = customer.objects.get(cust_id = request.session['cust_id']))
#     o.save()
#     order = order.objects.latest('ordermodel_id')
#     prods = shoppingcart.objects.all().filter(cart_cust_id = customer.objects.get(cust_id = request.session['cust_id']))
#     for prod in prods:
#         id = prod.cart_prod_id.prod_id
#         o_item = orderitem(orderitem_ordermodel_id=order, orderitem_prod_id=product.objects.get(prod_id=id))
#         o_item.save()
#     for prod in prods:
#         prod.delete()
#     return render(request, 'confirmorder.html')

# def confirmorderB(request):
#     o = ordermodel(ordermodel_cust_id = customer.objects.get(cust_id = request.session['cust_id']))
#     o.save()
#     order = ordermodel.objects.last()
#     p_id = request.GET['p_id']
#     prod = product.objects.get(prod_id = p_id)
#     o_item = orderitem(orderitem_ordermodel_id=order, orderitem_prod_id=prod)
#     o_item.save()
#     return render(request, 'confirmorder.html')