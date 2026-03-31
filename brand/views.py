from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand
from .forms import BrandForm
from django.http import HttpResponse
from django.http import HttpRequest
# Create your views here.


def get_brands(request):
    brands = Brand.objects.all()
    return render(request,'brand/index.html', {'brands':brands})


def post_brand(request:HttpRequest):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brands:index')
    context = {
        'form': BrandForm()
    }
    return render(request, 'brand/create.html', context)

def delete_brand(request:HttpRequest, id):
    brand = get_object_or_404(Brand, id=id)
    brand.delete()
    return redirect('brands:index')

def update_brand(request:HttpRequest, id):
    brand = get_object_or_404(Brand, id=id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brands:index')
    form = BrandForm(instance=brand)
    context = {
        'form': form
    }
    return render(request, 'brand/update.html', context)
    


