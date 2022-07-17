from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from shop.models import *

# Create your views here.

def index(request):
    context={

    }
    return render(request, 'shop/index.html', context)

def about(request):
    context={}
    return render(request, 'shop/about-us.html', context)

def myaccount(request):
    context={}
    return render(request, 'shop/myaccount.html', context)

def blog(request):
    context={}
    return render(request, 'shop/blog.html', context)

def shop(request):
    context={}
    return render(request, 'shop/shop.html', context)

def productdetail(request):
    productdetail = get_object_or_404(Product)
    context={
        'productdetail':productdetail,
    }
    return render(request, 'shop/productdetail.html', context)

def viewcart(request):
    context={}
    return render(request, 'shop/cart_page.html', context)

def checkout(request):
    context={}
    return render(request, 'shop/checkout.html', context)
    

def contact(request):
    if request.method == "POST":
        fullname = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        form = Contact(FullName=fullname, Subject=subject, Email=email, Message=message)
        messages.success(request, 'Thank you. We will contact you soon.')
        form.save()
        
    return render(request, 'shop/contact.html')

def login_register(request):
    context={}
    return render(request, 'shop/login_register.html', context)