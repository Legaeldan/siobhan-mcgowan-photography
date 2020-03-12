from django.db import models
from django.utils import timezone

# Create your models here.
class Photo(models.Model):
    class Meta:
        ordering = ['published_date']
    name = models.CharField(max_length=150, default='Photograph')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name