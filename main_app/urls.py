from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('guitars/', views.GuitarList.as_view(), name="guitar_list"),
    path('guitars/new/', views.GuitarCreate.as_view(), name="guitar_create"),
    path('guitars/<int:pk>/', views.GuitarDetail.as_view(), name="guitar_detail"),
    path('guitars/<int:pk>/update',views.GuitarUpdate.as_view(), name="guitar_update"),
    path('guitars/<int:pk>/delete',views.GuitarDelete.as_view(), name="guitar_delete"),
    path('guitars/<int:pk>/artists/new/', views.ArtistCreate.as_view(), name="artist_create"),
    path('genres/<int:pk>/artists/<int:artist_pk>/', views.GenreArtistAssoc.as_view(), name="genre_artist_assoc"),
]