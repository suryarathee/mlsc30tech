from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Offers

# Create your views here.


def index(request):
    products =Product.objects.all()
    offers =Offers.objects.all()
    return render(request,'index.html',{'products':products,'offers':offers})


def new(request):
    return HttpResponse("THIS IS NEW FUNCTION")



