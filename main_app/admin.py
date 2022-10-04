from django.contrib import admin
from .models import Guitar # import the Guitar model from models.py
# Register your models here.

admin.site.register(Guitar) # this line will add the model to the admin panel
