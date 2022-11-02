# Generated by Django 4.1.3 on 2022-11-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('display_name', models.CharField(default=models.CharField(max_length=20), max_length=20)),
                ('private', models.BooleanField(default=True)),
            ],
        ),
    ]
