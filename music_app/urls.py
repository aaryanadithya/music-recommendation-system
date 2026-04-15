from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/search/', views.search_songs, name='search_songs'),
    path('api/songs/', views.get_all_songs, name='get_all_songs'),
]

# project/urls.py (main urls.py)
