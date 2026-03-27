from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.


def get_cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


def post_car(request):
    return render(request, 'cars/create.html')