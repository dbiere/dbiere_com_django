from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('media_diet', views.media_diet, name='media_diet'),
]

