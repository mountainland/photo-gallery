# Generated by Django 4.1.3 on 2022-11-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
