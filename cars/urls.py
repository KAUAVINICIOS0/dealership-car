from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path("", views.get_cars, name="index"),
    path("create/", views.post_car, name='create_car'),
    path("delete/<int:id>", views.delete_car, name='delete_car'),
    path("update/<int:id>", views.update_car, name='update_car'),
]