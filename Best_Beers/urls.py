"""
URL configuration for Best_Beers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from beers.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_beers, name='beer_list'),
    path('beers/', get_beers, name='beer_list'),
    path('breweries/', get_breweries, name='get_breweries'),
    path('categories/', get_categories, name='get_categories'),
    path('styles/', get_styles, name='get_styles'),
]
