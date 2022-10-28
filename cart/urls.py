from unicodedata import name
from django.urls import path
from . import views


urlpatterns= [
    path('',views.kart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name="add_cart"),  
]