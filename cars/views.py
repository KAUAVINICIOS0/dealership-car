from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car
from .forms import CarForm
from django.http import HttpRequest
# Create your views here.


def get_cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


def post_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:index')
    context = {
        'form': CarForm()
    }
    return render(request, 'cars/create.html', context)