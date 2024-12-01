from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date = models.DateField()
    gender = models.CharField(max_length=25)
    address = models.TextField()
