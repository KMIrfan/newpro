from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customtemp/index.html')