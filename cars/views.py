from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_cars(request):
    context = {
        'cars': Car.objects.all()
    }
    return render(request, 'cars/index.html', context)
