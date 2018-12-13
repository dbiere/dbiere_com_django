from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def learning(request):
    return render(request, 'main/learning.html')

def media_diet(request):
    return render(request, 'main/media_diet.html')

def resume(request):
    return render(request, 'main/resume.html')

def data_viz(request):
    return render(request, 'main/data_viz.html')