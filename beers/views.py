from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from beers.forms import GeocodeForm
from beers.models import *


def brewery(request, pk):
    b = Brewery.objects.get(id=pk)
    location = BreweryGeocode.objects.get(brewery_id=pk)
    form = GeocodeForm(request.POST or None, instance=location)
    return render(request, 'brewery.html', {'page_title': 'Brewery',
                                            'brewery': b,
                                            'location': location,
                                            'form': form
                                            })
