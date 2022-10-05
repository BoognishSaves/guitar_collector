from django.contrib import admin
from .models import Guitar # import the Guitar model from models.py
from .models import Artist, Genre
# Register your models here.

admin.site.register(Guitar) # this line will add the model to the admin panel
admin.site.register(Artist)
admin.site.register(Genre)