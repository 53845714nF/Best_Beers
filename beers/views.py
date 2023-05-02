from django.shortcuts import render
from django.http import HttpResponse
from beers.models import *


def get_beers(request):
    beers = Beer.objects.all().order_by('id')[:50]

    return render(request, 'list_beer.html', {'page_title': 'Best Beers',
                                              'beers': beers, })


def get_breweries(request):
    breweries = Brewery.objects.all().order_by('id')[:50]
    return render(request, 'list_breweries.html', {'page_title': 'Breweries',
                                                   'breweries': breweries, })


def get_categories(request):
    categories = Category.objects.all().order_by('id')
    return render(request, 'list_categories.html', {'page_title': 'Categories',
                                                    'categories': categories, })


def get_styles(request):
    styles = Style.objects.all().order_by('id')
    return render(request, 'list_styles.html', {'page_title': 'Styles',
                                                'styles': styles, })
