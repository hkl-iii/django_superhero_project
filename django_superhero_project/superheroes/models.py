from django.db import models


# Create your models here.

class Superhero(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    runtime = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.name
