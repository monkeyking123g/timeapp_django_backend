from django.db import models


class Time(models.Model):
    datetime_add =  models.DateTimeField(blank=True, null=True)
    ore_lavorative =  models.FloatField()
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{str(self.datetime_add)} -- {str(self.ore_lavorative)} -- {str(self.owner)}'

class Totale(models.Model):
    datetime_add =  models.DateTimeField(auto_now_add=True)
    total_ore =  models.FloatField()
    owner = models.ForeignKey('auth.User', related_name='snippetsq', on_delete=models.CASCADE)
   
    def __str__(self):
        return f'{str(self.datetime_add)} -- {str(self.total_ore)} -- {str(self.owner)}'

