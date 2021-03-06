from django.shortcuts import render
from photos.models import Photo
from django.db.models import Q
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

def do_search(request):
    """
    Searches all available items in db for containing search query.
    Searches category, name, and tags.
    """
    photos = Photo.objects.filter(Q(name__icontains=request.GET['q']) | Q(category__name__icontains=request.GET['q']) | Q(tags__icontains=request.GET['q']))
    return render(request, "photos.html", {"photos": photos})