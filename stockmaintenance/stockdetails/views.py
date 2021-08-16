from django.shortcuts import render
from django.http import HttpResponse
from .models import Stock


# Create your views here.

def home(request):
    return render(request, 'stockdetails/home.html')


def index(request):
    stocks = Stock.objects.all()
    return render(request, 'stockdetails/index.html', {'stock': stocks})

