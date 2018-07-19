from djgeojson.fields import PolygonField
from django.db import models
import sys
sys.path.insert(0, '../src')
import time
from src.routing import single_source_routing

class MushroomSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = PolygonField()

    def __unicode__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture_url
