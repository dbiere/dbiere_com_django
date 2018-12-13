from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='books'),    # for /media_diet/books path
 
]
