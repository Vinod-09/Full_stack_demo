from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    category_name = models.CharField(max_length=255)

class Movies_dis(models.Model):
    movie_name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)

    