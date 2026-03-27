from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path("", views.get_cars),
    path("create/", views.post_car, name='create_car')
]