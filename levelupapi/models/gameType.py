from django.db import models
from django.urls import path, include


class GameType(models.Model):
    type = models.CharField(max_length=50)