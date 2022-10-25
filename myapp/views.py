from contextlib import redirect_stderr
from contextvars import Context
import http
import imp
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

from myapp.models import Product

# Create your views here.

def index(request):
    li = ['allen','sam','savis']
    context = {'names':li}
    return render(request, 'myapp/index.html', context = context)

def new_one(request):
    return HttpResponse('this is new one')


def products(request):
    p = Product.objects.all()
    # p1 = [Product.objects.get(id=2)]
    # p2 = Product.objects.filter(price__lt = 200000)

    # return HttpResponse(p[0].price)
    # return HttpResponse(p2)
    # print(p)
    # print(type(p[0]))

    context = {'products':p}
    return render(request, 'myapp/products.html', context = context)


def product_details(request, id):
    p = Product.objects.get(id = id)
    context = {'p':p}
    return render(request, 'myapp/product_details.html', context = context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']

        p = Product(name=name, price=price, description=desc, image=image)
        p.save()

        return redirect('/myapp/products')
    
    return render(request, 'myapp/add_product.html')












def assignment_1(request):
    return render(request, 'assignment.html')