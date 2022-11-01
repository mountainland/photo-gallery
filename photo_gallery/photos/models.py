from django.db import models
from galleries.models import Gallery

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos')
    gallery = models.ForeignKey(Gallery, ondelete=models.CASCADE)
    info_text = models.CharField(max_length=20)