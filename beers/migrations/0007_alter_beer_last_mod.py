# Generated by Django 4.2 on 2023-05-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0006_alter_category_last_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='last_mod',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='%Y-%m-%d %H:%M:%S'),
        ),
    ]
