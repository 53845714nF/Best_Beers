from django.contrib import admin
from beers.models import *

admin.site.register(Brewery)
admin.site.register(BreweryGeocode)
admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Beer)

