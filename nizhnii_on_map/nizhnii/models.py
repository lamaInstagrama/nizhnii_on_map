from django.db import models


class InterestingPlacesModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
