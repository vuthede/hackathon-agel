from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as mushrooms_models
from . import view as mushroom_view

admin.site.register(mushrooms_models.MushroomSpot, LeafletGeoAdmin)