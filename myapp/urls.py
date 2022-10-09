from django.urls import path, include
from myapp.views import index, new_one

urlpatterns = [
    path('', index),
    path('new/', new_one)

]