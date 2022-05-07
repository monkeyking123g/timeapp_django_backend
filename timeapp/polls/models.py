
from django.db import models

class Time(models.Model):
    datetime_add =  models.DateTimeField(blank=True, null=True)
    ore_lavorative =  models.FloatField()

    def __str__(self):
        return f'{str(self.datetime_add)} -- {str(self.ore_lavorative)}'

class Totale(models.Model):
    datetime_add =  models.DateTimeField(auto_now_add=True)
    total_ore =  models.FloatField()
    def __str__(self):
        return f'{str(self.datetime_add)} -- {str(self.total_ore)}'

