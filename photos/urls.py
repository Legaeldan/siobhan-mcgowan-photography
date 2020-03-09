from django.conf.urls import url, include
from .views import all_photos

urlpatterns = [
    url(r'^$', all_photos, name='photos'),
]