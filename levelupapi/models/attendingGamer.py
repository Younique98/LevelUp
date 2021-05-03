from django.db import models
from levelupapi.models import Gamer
from levelupapi.models import Event



class AttendingGamer(models.Model):

    gamer = models.ForeignKey(
        Gamer, on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE
    )
    