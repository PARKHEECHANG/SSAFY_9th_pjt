from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    poster_path = models.URLField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    watchlater = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watchlater_movie')

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)