from cProfile import label

from django.db import models

# Create your models here.
# model forms  must have string constructor otherwise it wont create the form
class Customer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=25)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    def __str__(self):
        return self.name