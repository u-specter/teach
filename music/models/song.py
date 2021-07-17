from django.db import models
from .album import Album

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    image = models.URLField(blank=True,null=True)
    source = models.URLField()