# Generated by Django 5.0.6 on 2024-06-28 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caters_registration',
            old_name='Id_proof',
            new_name='id_proof',
        ),
        migrations.RenameField(
            model_name='restuarant_registration',
            old_name='cg_image',
            new_name='r_image',
        ),
        migrations.RenameField(
            model_name='restuarant_registration',
            old_name='ck_image',
            new_name='rk_image',
        ),
    ]
