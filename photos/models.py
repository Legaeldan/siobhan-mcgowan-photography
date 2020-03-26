from django.db import models
from django.utils import timezone
import re

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    timestamp = models.DateTimeField(blank=True, default=timezone.now)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    class Meta:
        ordering = ['published_date']
    name = models.CharField(max_length=150, default='Photograph')
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True)
    tags = models.CharField(max_length=150, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateTimeField(blank=True, default=timezone.now)
    image = models.ImageField(upload_to='images')
    previewimage = models.ImageField(upload_to='images/preview', blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    banner = models.BooleanField(default=False)
    
    def tags_as_list(self):
        return re.findall(r"[\w']+", self.tags)

    def __str__(self):
        return self.name