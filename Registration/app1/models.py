from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.EmailField(max_length=50)
    fname=models.CharField(max_length=50)

