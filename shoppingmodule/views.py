from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.template.context_processors import csrf
from shoppingmodule.models import product,shoppingcart,orderitems,order
from loginmodule.models import customer
import datetime
from django.utils import timezone

# Create your views here.

def viewhome(request):
    prods = product.objects.all()
    if 'cust_id' in request.session:
        citems = shoppingcart.objects.all().filter(cart_cust_id = customer.objects.get(cust_id = request.session['cust_id'])).count()
        request.session['cartitems'] = citems
    return render(request, 'home.html', {'prods': prods})

def viewaboutus(request):
    return render(request, 'aboutus.html')

def addtocart(request):
    p_id = request.GET['p_id']
    c = shoppingcart(cart_cust_id=customer.objects.get(cust_id = request.session['cust_id']), cart_prod_id=product.objects.get(prod_id = p_id))
    c.save()
    return HttpResponseRedirect('/shoppingmodule/')

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

def confirmorder(request):
    prods = shoppingcart.objects.all().filter(cart_cust_id = customer.objects.get(cust_id = request.session['cust_id']))
    subtotal = 0.0
    for prod in prods:
        subtotal = subtotal + prod.cart_prod_id.price
    subtotal = subtotal + 19.05
    o = order(order_cust_id=customer.objects.get(cust_id=request.session['cust_id']), price=subtotal)
    o.save()
    ord = order.objects.latest('order_id')
    
    for prod in prods:
        id = prod.cart_prod_id.prod_id
        o_item = orderitems(orderitems_order_id=ord, orderitems_prod_id=product.objects.get(prod_id=id))
        o_item.save()
    for prod in prods:
        prod.delete()
    return HttpResponseRedirect('/shoppingmodule/viewconfirmorder/')

def confirmorderb(request):
    p_id = request.GET['p_id']
    prod = product.objects.get(prod_id = p_id)
    subtotal = prod.price + 19.05
    o = order(order_cust_id=customer.objects.get(cust_id=request.session['cust_id']), price=subtotal)
    o.save()
    ord = order.objects.latest('order_id')
    o_item = orderitems(orderitems_order_id=ord, orderitems_prod_id=prod)
    o_item.save() 
    return HttpResponseRedirect('/shoppingmodule/viewconfirmorder/')
    
def viewconfirmorder(request):
    return render(request, 'confirmorder.html')

def viewprofile(request):
    cust = customer.objects.get(cust_id = request.session['cust_id'])
    context = {
        'cust': cust
    }
    return render(request, 'profile.html', context)

def changeaddress(request):
    return render(request, 'changeaddress.html')

def addnewaddress(request):
    addr = request.POST['newaddress']
    cust = customer.objects.get(cust_id = request.session['cust_id'])
    cust.address = addr
    cust.save()
    return HttpResponseRedirect('/shoppingmodule/viewprofile/')

def changepassword(request):
    return render(request, 'changepassword.html')

def updatepassword(request):
    oldpass = request.POST['oldpass']
    newpass = request.POST['newpass']
    cnewpass = request.POST['cnewpass']
    u = User.objects.get(username=request.session['cust_name'])
    if not check_password(oldpass, u.password):
        return render(request, 'changepassword.html', {'msg': "*Old password is incorrect"})
    elif(newpass != cnewpass):
        return render(request, 'changepassword.html', {'msg': "*New passwords does not match"})
    else:
        user = User.objects.get(username=request.session['cust_name'])
        user.set_password(newpass)
        user.save()
        cust = customer.objects.get(cust_id=request.session['cust_id'])
        cust.password = newpass
        cust.save()
        return HttpResponseRedirect('/shoppingmodule/viewprofile/')

def vieworders(request):
    ords = order.objects.all().filter(order_cust_id=customer.objects.get(cust_id=request.session['cust_id']))
    date = timezone.now()
    for o in ords:
        if(date >= o.deliverdate):
            o.status = "delivered"
            o.save()
    items = []
    for o in ords:
        items.append(orderitems.objects.all().filter(orderitems_order_id=o))
    mylist = zip(items,ords)
    if 'cancel' in request.session:
        context = {
            'list': mylist,
            'cancelmsg': "Order cancelled successfully"
        }
        del request.session['cancel']
    else:
        context = {
        'list': mylist
        }
    return render(request, 'previousorders.html', context)

def cancelorder(request):
    oid = request.GET['o']
    ord = order.objects.get(order_id=oid)
    orditem = orderitems.objects.all().filter(orderitems_order_id=ord)
    for o in orditem:
        o.delete()
    ord.delete()
    request.session['cancel'] = "cancelled"
    return HttpResponseRedirect('/shoppingmodule/vieworders/')