from django.urls import path
from .import views

app_name = 'common'

urlpatterns = [
    path('', views.common_home, name = 'index'),
    path('customerlogin', views.customer_login, name = 'customer_login'),
    path('sellerlogin', views.seller_login, name = 'seller_login'),
    path('coadminlogin', views.coadmin_login, name = 'coadmin_login')
]