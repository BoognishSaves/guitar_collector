from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
# import models
from .models import Guitar

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(View):

    # Here we are adding a method that will be ran when we are dealing with a GET request
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Guitar Collector Home")

class About(TemplateView):
    template_name = "about.html"

class Home(TemplateView):
    template_name = "home.html"




class GuitarList(TemplateView):
    template_name = "guitar_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["guitars"] = Guitar.objects.filter(name__icontains=name)
        else:
            context["guitars"] = Guitar.objects.all()
        return context
