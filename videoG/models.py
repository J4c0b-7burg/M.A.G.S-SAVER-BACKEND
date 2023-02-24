from django.db import models

class Videog(models.Model):
    title = models.CharField(max_length=100)
    rating = models.CharField(max_length=2)
    image = models.CharField(max_length=500)
    completed = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

