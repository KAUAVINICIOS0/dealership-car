from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cars_home(request):
    context = {
        "name": "voyage",
    }
    return render(request, 'cars/index.html', context)
