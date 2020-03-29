from django.shortcuts import render
from photos.models import Photo
from django.db.models import Q
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
def do_search(request):
    photos = Photo.objects.filter(Q(name__icontains=request.GET['q']) | Q(category__name__icontains=request.GET['q']) | Q(tags__icontains=request.GET['q']))
    return render(request, "photos.html", {"photos": photos})