from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('guitars/', views.GuitarList.as_view(), name="guitar_list"),
    path('guitars/new/', views.GuitarCreate.as_view(), name="guitar_create"),
    path('guitars/<int:pk>/', views.GuitarDetail.as_view(), name="guitar_detail"),
    path('artists/<int:pk>/update',views.GuitarUpdate.as_view(), name="guitar_update"),
]