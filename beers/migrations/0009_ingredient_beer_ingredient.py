# Generated by Django 4.2 on 2023-05-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0008_alter_brewery_last_mod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='ingredient',
            field=models.ManyToManyField(to='beers.ingredient'),
        ),
    ]
