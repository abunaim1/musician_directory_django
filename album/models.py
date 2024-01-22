from django.db import models
from musician.models import Musician
# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length = 50, verbose_name = 'Album Name')
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    CHOICES = [('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5')]
    rating = models.CharField(max_length = 50, choices=CHOICES)

    def __str__(self) -> str:
        return self.album_name
