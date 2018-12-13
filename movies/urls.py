from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='movies'),    # for /media_diet/movies path
]
