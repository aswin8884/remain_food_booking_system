# Generated by Django 5.0.6 on 2024-06-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_restauarant_registration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restauarant_registration',
            name='closing_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='restauarant_registration',
            name='opening_time',
            field=models.TimeField(null=True),
        ),
    ]
