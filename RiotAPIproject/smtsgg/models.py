from django.db import models
from django.utils import timezone
from django.urls import reverse
 
# Create your models here.

class SearchCount(models.Model):
    puuid = models.CharField(max_length=70, primary_key=True)
    gamename = models.CharField(max_length=30)
    tagline = models.CharField(max_length=10)
    count = models.IntegerField(default=1)
    latest_search = models.TimeField(default=timezone.now())

    def __str__(self):
        return "#".join([self.gamename, self.tagline])
    
    def get_absolute_url(self):
        return reverse("model_detail", args=str(self))
    
