from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import MovieList, Movie
from .serializers import MovieListSerializer, MovieSerializer
from django.shortcuts import get_object_or_404
import requests

def index(request):
    return render(request, 'movies/index.html')

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    from django.contrib.auth import authenticate
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_movie_list(request):
    serializer = MovieListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_movie_lists(request):
    movie_lists = MovieList.objects.filter(user=request.user)
    serializer = MovieListSerializer(movie_lists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_movie_list(request, pk):
    movie_list = get_object_or_404(MovieList, pk=pk, user=request.user)
    serializer = MovieListSerializer(movie_list)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_movie_list(request, pk):
    movie_list = get_object_or_404(MovieList, pk=pk, user=request.user)
    serializer = MovieListSerializer(movie_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_movie_list(request, pk):
    movie_list = get_object_or_404(MovieList, pk=pk, user=request.user)
    movie_list.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_movie(request):
    title = request.data.get('title')
    api_key = '3cf5f2f'
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return Response(response.json())
    return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_movie_to_list(request, pk):
#     movie_list = get_object_or_404(MovieList, pk=pk, user=request.user)
#     title = request.data.get('title')
#     year = request.data.get('year')
#     imdb_id = request.data.get('imdb_id')
#     movie = Movie(title=title, year=year, imdb_id=imdb_id, movie_list=movie_list)
#     movie.save()
#     return Response({'message': 'Movie added to list'}, status=status.HTTP_201_CREATED)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_movie_to_list(request, pk):
    movie_list = get_object_or_404(MovieList, pk=pk, user=request.user)
    title = request.data.get('title')
    year = request.data.get('year')
    imdb_id = request.data.get('imdbID')
    
    print(f"Title: {title}, Year: {year}, IMDb ID: {imdb_id}")  # Debugging log
    
    if not title or not year or not imdb_id:
        return Response({'error': 'Title, year, and IMDb ID are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    movie = Movie(title=title, year=year, imdb_id=imdb_id, movie_list=movie_list)
    movie.save()
    return Response({'message': 'Movie added to list'}, status=status.HTTP_201_CREATED)
