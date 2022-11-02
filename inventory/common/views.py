from django.shortcuts import render

# Create your views here.
def common_home(request):
    return render(request, 'demo/index.html')

def customer_login(request):
    return render(request, 'demo/customer.html')  

def seller_login(request):
    return render(request, 'demo/seller.html')  

def coadmin_login(request):
    return render(request, 'demo/coadmin.html')      