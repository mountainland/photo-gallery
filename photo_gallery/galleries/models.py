from django.db import models

class Gallery(models.Model):
    gallery_name = models.CharField(max_length=20)
    private = models.BooleanField(default=True)