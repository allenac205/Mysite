from django.urls import path, include
from myapp.views import index, new_one, products, product_details, add_product, update_product, delete_product, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDelete, cart_add, cart_view, cart_remove, oder_summary, payment_success, oder_history


app_name = 'myapp'

urlpatterns = [
    path('', index),
    path('new/', new_one),
    # path('products/', products, name='products'),
    path('products/', ProductListView.as_view(), name='products'),
    # path('products/<int:id>', product_details, name='product_details'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('products/add', add_product, name='add_product'),
    # path('products/add', ProductCreateView.as_view(), name='add_product'),
    path('products/update/<int:id>', update_product, name='update_product'),
    # path('products/update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:id>', delete_product, name='delete_product'),
    # path('products/delete/<int:pk>', ProductDelete.as_view(), name='delete_product'),
    path('cart_add/<int:id>', cart_add, name='cart_add'),
    path('cart_view', cart_view, name='cart_view'),
    path('cart_remove/<int:id>', cart_remove, name='cart_remove'),
    path('oder_summary', oder_summary, name='oder_summary'),
    path('payment_success', payment_success, name='payment_success'),
    path('oder_history', oder_history, name='oder_history'),

]