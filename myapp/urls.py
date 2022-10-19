from django.urls import path, include
from myapp.views import index, new_one, products, assignment_1, product_details,add_product

urlpatterns = [
    path('', index),
    path('new/', new_one),
    path('products/', products),
    path('assignment1/', assignment_1, name='products'),
    path('products/<int:id>', product_details, name='product_details'),
    path('products/add', add_product, name='add_product')

]