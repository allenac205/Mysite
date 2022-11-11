from django.urls import path, include
from myapp.views import index, new_one, products, assignment_1, product_details, add_product, update_product, delete_product, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDelete


app_name = 'myapp'

urlpatterns = [
    path('', index),
    path('new/', new_one),
    # path('products/', products, name='products'),
    path('products/', ProductListView.as_view(), name='products'),
    path('assignment1/', assignment_1,),
    # path('products/<int:id>', product_details, name='product_details'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('products/add', add_product, name='add_product'),
    # path('products/add', ProductCreateView.as_view(), name='add_product'),
    path('products/update/<int:id>', update_product, name='update_product'),
    # path('products/update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:id>', delete_product, name='delete_product'),
    # path('products/delete/<int:pk>', ProductDelete.as_view(), name='delete_product')
]