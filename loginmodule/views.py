from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from .models import customer
# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        c = customer.objects.get(username=request.POST['username'])
        c.password = password
        c.save()
        request.session['cust_id'] = c.cust_id
        request.session['cust_name'] = c.username
        return HttpResponseRedirect('/shoppingmodule/')
    else:
        return HttpResponseRedirect('/loginmodule/invalidlogin/')

def register_user(request):
    return render(request, 'register.html')

def register(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    cpassword = request.POST.get('cpassword', '')
    email = request.POST.get('email', '')
    address = request.POST.get('address', '')
    if(password != cpassword):
        return render(request, 'register.html', {'msg': "*Passwords doesn't match"})
    newuser = customer.objects.filter(username=username).first()
    if newuser is not None:
        return render(request, 'register.html', {'msg': "*username already taken"})
    cust = customer(username = username, address = address, email = email, password = password)
    cust.save()
    user = User.objects.create_user(username = username, email = email, password = password)
    return HttpResponseRedirect('/loginmodule/login/')

def loggedin(request):
    return render(request, 'loggedin.html', {"full_name":request.user.username})

def invalidlogin(request):
    return render(request, 'invalidlogin.html')

def logout(request):
    del request.session['cust_id']
    del request.session['cust_name']
    auth.logout(request)
    return render(request, 'logout.html')
