from django.shortcuts import render
from photos.models import Photo

# Create your views here.
def do_search(request):
    photos = Photo.objects.filter(name__icontains=request.GET['q'])
    return render(request, "photos.html", {"photos": photos})