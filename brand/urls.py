from django.urls import path
from . import views

app_name = 'brands'

urlpatterns  = [
    path('', views.get_brands, name='index')
]