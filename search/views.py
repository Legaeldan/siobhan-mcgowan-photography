from django.shortcuts import render
from photos.models import Photo
from django.db.models import Q

# Create your views here.
def do_search(request):
    photos = Photo.objects.filter(Q(name__icontains=request.GET['q']) | Q(category__name__icontains=request.GET['q']))
    return render(request, "photos.html", {"photos": photos})