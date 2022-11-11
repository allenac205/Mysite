
from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'name', 'price', 'description', 'image', 'seller' ]
