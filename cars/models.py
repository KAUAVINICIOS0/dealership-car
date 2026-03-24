from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name