from django.urls import path
from . import views

app_name = 'brands'

urlpatterns  = [
    path('', views.get_brands, name='index'),
    path('create/', views.post_brand, name='create_brand'),
    path('delete/<int:id>', views.delete_brand, name='delete_brand'),

]