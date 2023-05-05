from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from location_field.models.plain import PlainLocationField


class Brewery(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=100)
    code = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    phone = models.CharField(max_length=40)
    website = models.CharField(max_length=40)
    description = models.CharField(max_length=1024)
    last_mod = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class AccuracyEnum(ChoiceEnum):
    ROOFTOP = 'Rooftop'
    RANGE_INTERPOLATED = 'Range Interpolated'
    GEOMETRIC_CENTER = 'Geometric Center'
    APPROXIMATE = 'Approximate'


class BreweryGeocode(models.Model):
    brewery_id = models.ForeignKey(Brewery, on_delete=models.SET_NULL, null=True)
    location = PlainLocationField(based_fields=['city'], zoom=5)
    accuracy = EnumChoiceField(AccuracyEnum)

    def __str__(self):
        return f'({self.brewery_id} at {self.location})'


class Category(models.Model):
    name = models.CharField(max_length=30)
    last_mod = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Style(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    last_mod = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Beer(models.Model):
    name = models.CharField(max_length=50)
    brewery_id = models.ForeignKey(Brewery, on_delete=models.SET_NULL, null=True)
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    style_id = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True)
    alcohol_by_volume = models.FloatField(null=False, default=0)
    description = models.CharField(max_length=1000)
    last_mod = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
