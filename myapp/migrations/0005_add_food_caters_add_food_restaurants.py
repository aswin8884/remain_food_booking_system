# Generated by Django 5.0.6 on 2024-06-29 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_restauarant_registration_closing_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_food_caters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('food_image', models.ImageField(null=True, upload_to='')),
                ('uploaded_time', models.DateTimeField(null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('caters_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.caters_registration')),
            ],
        ),
        migrations.CreateModel(
            name='Add_food_restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('food_image', models.ImageField(null=True, upload_to='')),
                ('uploaded_time', models.DateTimeField(null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('restaurant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.restauarant_registration')),
            ],
        ),
    ]
