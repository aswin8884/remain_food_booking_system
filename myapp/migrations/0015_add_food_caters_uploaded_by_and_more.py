# Generated by Django 5.0.6 on 2024-07-01 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_add_food_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_food_caters',
            name='uploaded_by',
            field=models.CharField(default='caters', max_length=50),
        ),
        migrations.AddField(
            model_name='add_food_restaurants',
            name='uploaded_by',
            field=models.CharField(default='restaurant', max_length=50),
        ),
    ]
