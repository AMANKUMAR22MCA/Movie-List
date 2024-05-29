from rest_framework import serializers
from .models import MovieList, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'imdb_id', 'movie_list']

class MovieListSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = MovieList
        fields = ['id', 'name', 'is_public', 'user', 'movies']
