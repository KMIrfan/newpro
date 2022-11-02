from django.urls import path
from .import views

app_name = 'coadmin'

urlpatterns = [
    path('index', views.coadmin_home, name='coadmin_home'),
   
]