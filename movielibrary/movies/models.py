from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class MovieList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    imdb_id = models.CharField(max_length=20)
    movie_list = models.ForeignKey(MovieList, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
