# Generated by Django 5.0.6 on 2024-06-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_add_food_caters_add_food_restaurants'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_food_restaurants',
            name='admin_accept_time',
            field=models.DateTimeField(null=True),
        ),
    ]
