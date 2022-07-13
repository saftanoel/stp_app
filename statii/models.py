from django.db import models

# Create your models here.

from django.db import models


class Statie(models.Model):
    nume = models.CharField(max_length=255)
    StatieID = models.IntegerField()
    long = models.FloatField()
    lat = models.FloatField()
    class Meta:
        verbose_name_plural="Statii"

    def __str__(self):
        return self.nume

class Autobuz(models.Model):
    long = models.FloatField()
    lat = models.FloatField()
    idBus = models.IntegerField()
    nrInm = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="Autobuze"

    def __str__(self):
        return self.nrInm
