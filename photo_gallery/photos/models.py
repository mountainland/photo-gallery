from django.db import models


class Photo(models.Model):
    photo_path = models.CharField(max_length=200)
    gallery = models.ForeignKey(Gallery, ondelete=models.CASCADE)
    info_text = models.CharField(max_length=20)