from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=9)



class Cart(models.Model):

    def __str__(self):
        return self.product_name

    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    


class OderHistory(models.Model):

    def __str__(self):
        return self.product_name

    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

