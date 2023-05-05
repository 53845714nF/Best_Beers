from django.shortcuts import render, get_object_or_404, redirect

from beers.models import *

def get_breweries(request):
    breweries = Brewery.objects.all().order_by('id')[:50]
    return render(request, 'list_breweries.html', {'page_title': 'Breweries',
                                                   'breweries': breweries, })


def brewery(request, pk):
    b = Brewery.objects.get(id=pk)
    location = BreweryGeocode.objects.get(brewery_id=pk)
    return render(request, 'brewery.html', {'page_title': 'Brewery',
                                            'brewery': b,
                                            'location': location,
                                            })