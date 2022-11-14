from django.urls import path
from account import views


urlpatterns= [
    path('register/',views.Registration, name='register'),
    path('login/',views.LoginView, name='login'),
    path('logout/',views.LogoutView, name='logout'),
]