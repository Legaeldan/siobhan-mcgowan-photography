from django.db import models
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=180)
    timestamp = models.DateTimeField(blank=True, default=timezone.now)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name