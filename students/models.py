from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length = 100)
    license_plate = models.PositiveIntegerField()
    studentt_name = models.CharField(max_length=100)
    passenger_capacity = models.PositiveIntegerField()
    car_model = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
