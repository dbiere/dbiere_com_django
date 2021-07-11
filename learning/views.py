from django.shortcuts import render

from .models import Training

def index(request):

    # Retrieve data

    # Add to context
    context = {}

    # Route request
    return render(request, 'learning/index.html', context)
