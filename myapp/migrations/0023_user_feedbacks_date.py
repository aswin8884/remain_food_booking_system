# Generated by Django 5.0.6 on 2024-07-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_user_feedbacks'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_feedbacks',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
