from django.urls import path
from .views import register_user, login_user, create_movie_list, view_movie_lists, view_movie_list, update_movie_list, delete_movie_list, search_movie, add_movie_to_list
from .views import index
urlpatterns = [
    path('home/', index, name='index'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('movie_lists/', view_movie_lists, name='view_movie_lists'),
    path('movie_lists/create/', create_movie_list, name='create_movie_list'),
    path('movie_lists/<int:pk>/', view_movie_list, name='view_movie_list'),
    path('movie_lists/<int:pk>/update/', update_movie_list, name='update_movie_list'),
    path('movie_lists/<int:pk>/delete/', delete_movie_list, name='delete_movie_list'),
    path('movie_lists/<int:pk>/add_movie/', add_movie_to_list, name='add_movie_to_list'),
    path('search/', search_movie, name='search_movie'),
]
