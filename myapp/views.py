from contextvars import Context
import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    li = ['allen','sam','savis']
    context = {'names':li}
    return render(request, 'listing/index.html', context = context)

def new_one(request):
    return HttpResponse('this is new one')