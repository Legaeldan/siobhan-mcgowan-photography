from django.shortcuts import render
from .models import Photo

# Create your views here.
def all_photos(request):
    photos = Photo.objects.all()
    return render(request, "photos.html", {"photos": photos})