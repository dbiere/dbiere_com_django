from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_viz', views.data_viz, name='data_viz'),
    path('learning', views.learning, name='learning'),
    path('media_diet', views.media_diet, name='media_diet'),
    path('resume', views.resume, name='resume'),
]

