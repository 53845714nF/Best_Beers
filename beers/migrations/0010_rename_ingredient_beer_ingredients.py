# Generated by Django 4.2 on 2023-05-06 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0009_ingredient_beer_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]