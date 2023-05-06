# Generated by Django 4.2 on 2023-05-05 12:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0003_alter_style_last_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='last_mod',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='%Y-%m-%d %H:%M:%S'),
        ),
    ]
