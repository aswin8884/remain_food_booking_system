# Generated by Django 5.0.6 on 2024-07-02 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_user_booking_food_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=250, null=True)),
                ('rating', models.IntegerField(null=True)),
                ('booking_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user_booking_food')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user_registration')),
            ],
        ),
    ]
