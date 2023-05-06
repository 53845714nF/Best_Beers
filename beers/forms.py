from django import forms
from location_field.forms.plain import PlainLocationField

from beers.models import *


class GeocodeForm(forms.ModelForm):
    class Meta:
        model = BreweryGeocode
        fields = ['location']
