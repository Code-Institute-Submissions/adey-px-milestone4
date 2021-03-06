from django.shortcuts import render, redirect
from music.models import Audio
from profiles.models import UserProfile

# Create your views here.


# Home page view that renders all audio from db
def index(request):
    """ A view that renders home page with all audio songs """
    songs = Audio.objects.all()

    context = {
        "songs": songs,
    }

    return render(request, 'home/index.html', context)
