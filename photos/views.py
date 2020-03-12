from django.shortcuts import render, get_object_or_404
from .models import Photo
from watermarker.models import Watermark

# Create your views here.
def all_photos(request):
    photos = Photo.objects.all()
    return render(request, "photos.html", {"photos": photos})

def photo_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, "photo-detail.html", {'photo': photo})