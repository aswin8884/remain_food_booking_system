# Generated by Django 5.0.6 on 2024-07-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_user_booking_food_address_user_booking_food_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_booking_food',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
