from django.urls import path
from .import views

app_name = 'seller'

urlpatterns = [
    path('index', views.seller_home, name='seller_home'),
   
]