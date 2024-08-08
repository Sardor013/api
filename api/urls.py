from django.urls import path
from .views import ArtistAPIView, AlbomAPIView, SongAPIView, SongDetailAPIView, AlbomDetailAPIView, ArtistDetailAPIView, Artist

urlpatterns = [
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path('albom/', AlbomAPIView.as_view(), name='album'),
    path('song/', SongAPIView.as_view(), name='song'),
    path('song/<int:id>/', SongDetailAPIView.as_view(), name='song-detail'),
    path('albom/<int:id>/', AlbomDetailAPIView.as_view(), name='albom-detail'),
    path('artist/<int:id>/', ArtistDetailAPIView.as_view(), name='artist-detail'),
]