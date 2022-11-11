from django.shortcuts import render
from myapp.models import Product
from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import ProductSerializer, UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer