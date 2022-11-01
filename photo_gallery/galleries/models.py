from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=20)
    display_name = models.CharField(max_length=20, default=name)
    private = models.BooleanField(default=True)