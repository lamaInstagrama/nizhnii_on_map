from django.db import models


class InterestingPlacesModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    group = models.ForeignKey('Groups', on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)

    def __str__(self):
        return self.name
