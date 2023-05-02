# Generated by Django 4.2 on 2023-04-29 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0004_beercategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerStyles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=50)),
                ('last_mod', models.CharField(max_length=20)),
                ('cat_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beers.beercategories')),
            ],
        ),
    ]