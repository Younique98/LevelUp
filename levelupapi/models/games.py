from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    