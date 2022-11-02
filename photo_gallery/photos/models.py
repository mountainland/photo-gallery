from django.db import models
from galleries.models import Gallery

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos')
    name = models.CharField(max_length=10)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    info_text = models.CharField(max_length=20)