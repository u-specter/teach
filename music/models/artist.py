from django.db import models
from general.models import Base

class Artist(Base):
    name = models.CharField(max_length=128)
    image = models.URLField(blank=True,null=True)