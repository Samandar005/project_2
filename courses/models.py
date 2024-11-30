from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    descriotion = models.TextField()
    start_data = models.DateField()
    end_data = models.DateField()
    max_students = models.PositiveIntegerField()