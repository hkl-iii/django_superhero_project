from django.db import models


# Create your models here.

class Superhero(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    runtime = models.IntegerField()
    release_date = models.DateField()
    image = models.ImageField(null=True, blank=True,upload_to='images/')

    def __str__(self):
        return self.name
