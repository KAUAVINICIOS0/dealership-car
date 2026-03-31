from django.shortcuts import render
from .models import Brand
# Create your views here.


def get_brands(request):
    brands = Brand.objects.all()
    return render(request,'brand/index.html', {'brands':brands})