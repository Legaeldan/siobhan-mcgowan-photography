from django.shortcuts import render
from photos.models import Photo

# Create your views here.
def index(request):
    """A view that displays the index page"""
    photos = Photo.objects.all()
    return render(request, "index.html", {"photos": photos})