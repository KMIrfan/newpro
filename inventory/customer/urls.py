from django.urls import path
from .import views

app_name = 'customer'

urlpatterns = [
    path('index', views.customer_home, name='customer_home'),
   
]