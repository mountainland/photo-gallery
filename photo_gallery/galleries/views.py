from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Gallery

def index(request):
    galleries_list = Gallery.objects.all().filter(private=False)
    
    context = {
        'galleries_list': galleries_list,
    }
    return render(request, 'galleries/index.html', context)
