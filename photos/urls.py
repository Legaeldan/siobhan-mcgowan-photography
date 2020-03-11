from django.conf.urls import url, include
from .views import all_photos, photo_detail

urlpatterns = [
    url(r'^$', all_photos, name='photos'),
    url(r'^(?P<pk>\d+)/$', photo_detail, name='photo_detail')
]