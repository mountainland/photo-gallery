# Generated by Django 4.1.3 on 2022-11-01 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_gallery_gallery_display_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='gallery_display_name',
            new_name='display_name',
        ),
    ]