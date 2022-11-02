from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.gallery, name='gallery'),
    path('photos/<str:photo>', views.read_photo, name='read_photo'),
]