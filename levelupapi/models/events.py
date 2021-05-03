from django.db import models
from django.contrib.auth.models import Gamer
from django.contrib.auth.models import Game


class Event(models.Model):

    event_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()
    gamer = models.ForeignKey(
        Gamer, on_delete=models.CASCADE)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE)