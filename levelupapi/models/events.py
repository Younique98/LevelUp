from django.db import models

class Event(models.Model):

    event_name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    organizer = models.ForeignKey(
        "Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE)
    attendee = models.ManyToManyField( "Gamer",
        related_name='attending', through='AttendingGamer'
    )
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value