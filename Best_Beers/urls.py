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
from django.urls import path, reverse_lazy
from django.views.generic import *

from beers.forms import GeocodeForm
from beers.views import *

urlpatterns = [
    # Default
    path('', ListView.as_view(model=Beer,
                              paginate_by=100,
                              extra_context={'page_title': "List Beers"}), name='beer_read'),
    # Admin
    path('admin/', admin.site.urls),

    # CRUD Brewery
    # TODO CU Brewery (no time)
    path('breweries/', ListView.as_view(model=Brewery,
                                        extra_context={'page_title': "List Breweries"}), name='brewery_read'),
    path('brewery/<pk>', brewery, name='brewery_update'),
    path('brewery/del/<pk>', DeleteView.as_view(model=Brewery,
                                                success_url=reverse_lazy('brewery_read'),
                                                extra_context={'page_title': "Delete Brewery"}), name='brewery_delete'),
    # CRUD Beer
    path('beer/', CreateView.as_view(model=Beer,
                                     fields=['name', 'brewery_id', 'cat_id', 'style_id', 'alcohol_by_volume',
                                             'description', 'ingredients'],
                                     success_url=reverse_lazy('beer_read'),
                                     extra_context={'page_title': "Create Beer"}), name='beer_create'),
    path('beers/', ListView.as_view(model=Beer,
                                    paginate_by=100,
                                    extra_context={'page_title': "List Beers"}), name='beer_read'),
    path('beer/<pk>', UpdateView.as_view(model=Beer,
                                         fields=['name', 'brewery_id', 'cat_id', 'style_id', 'alcohol_by_volume',
                                                 'description', 'ingredients'],
                                         success_url=reverse_lazy('beer_read'),
                                         extra_context={'page_title': "Update Beer"}), name='beer_update'),
    path('beer/del/<pk>', DeleteView.as_view(model=Beer,
                                             success_url=reverse_lazy('beer_read'),
                                             extra_context={'page_title': "Delete Beer"}),
         name='beer_delete'),

    # CRUD Categories
    path('category/', CreateView.as_view(model=Category,
                                         fields=['name'],
                                         success_url=reverse_lazy('category_read'),
                                         extra_context={'page_title': "Create Category"}), name='category_create'),
    path('categories/', ListView.as_view(model=Category,
                                         extra_context={'page_title': "List Categories"}), name='category_read'),
    path('category/<pk>', UpdateView.as_view(model=Category,
                                             fields=['name'],
                                             success_url=reverse_lazy('category_read'),
                                             extra_context={'page_title': "Update Category"}), name='category_update'),
    path('category/del/<pk>', DeleteView.as_view(model=Category,
                                                 success_url=reverse_lazy('category_read'),
                                                 extra_context={'page_title': "Delete Category"}),
         name='category_delete'),

    # CRUD Styles
    path('style/', CreateView.as_view(model=Style,
                                      fields=['name', 'cat_id'],
                                      success_url=reverse_lazy('style_read'),
                                      extra_context={'page_title': "Create Style"}), name='style_create'),
    path('styles/', ListView.as_view(model=Style,
                                     extra_context={'page_title': "List Styles"}), name='style_read'),
    path('style/<pk>', UpdateView.as_view(model=Style,
                                          fields=['name', 'cat_id'],
                                          success_url=reverse_lazy('style_read'),
                                          extra_context={'page_title': "Update Style"}), name='style_update'),
    path('style/del/<pk>', DeleteView.as_view(model=Style,
                                              success_url=reverse_lazy('style_read'),
                                              extra_context={'page_title': "Delete Style"}),
         name='style_delete'),
]
