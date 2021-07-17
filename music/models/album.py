from django.db import models
from .artist import Artist

class Album(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=128)
    image = models.URLField(blank=True,null=True)