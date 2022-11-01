from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Gallery

def index(request):
    galleries_list = Gallery.objects.all().filter(private=False)
    template = loader.get_template('galleries/index.html')
    
    context = {
        'galleries_list': galleries_list,
    }
    return HttpResponse(template.render(context, request))