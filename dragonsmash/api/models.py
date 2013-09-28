from django.db import models

DEFAULT_EFFECT_RADIUS = 20 # feet
DEFAULT_COUNTDOWN_TIME = 60 # seconds

class Client(models.Model):
    username = models.CharField(max_length=30)
    score = models.BigIntegerField(default=0)

    
class Effect(models.Model):
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    radius = models.IntegerField(default=DEFAULT_EFFECT_RADIUS)
    time_initiated = models.DateTimeField(auto_now=True)
    time_countdown = models.IntegerField(default=DEFAULT_COUNTDOWN_TIME)
    client_source = models.ForeignKey('Client')
        
