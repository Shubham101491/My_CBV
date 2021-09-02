from django.db import models
from django.urls import reverse

class School(models.Model):
    name = models.CharField(max_length=50)
    princlipal = models.CharField(max_length=50)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    # CreateView Part
    # we need this when url error shown then use 'reverse'

    # def get_absolute_url(self):
    #     return reverse("school:detail",kwargs={'pk':self.pk})
    # or use success_url in views.py

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name