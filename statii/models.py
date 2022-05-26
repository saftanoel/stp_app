from django.db import models

# Create your models here.

from django.db import models


class Statie(models.Model):
    nume = models.CharField(max_length=255)
    StatieID = models.IntegerField()
    long = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.nume
