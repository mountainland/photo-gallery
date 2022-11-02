from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

def index(request):
    return HttpResponse("test")


def gallery(request, name):
    photos = Photo.objects.all().filter(gallery__name=name)
    
    context = {
        'photos': photos
    }
    return render(request, 'photos/gallery.html', context=context)

def read_photo(request, photo):
    f = open(f'photos/{photo}', 'rb')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type=f"image/{photo.split('.')[-1]}")