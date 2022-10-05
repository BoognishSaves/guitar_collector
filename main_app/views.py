from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.shortcuts import redirect
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

# import models
from .models import Guitar, Artist, Genre

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        return context



class GuitarList(TemplateView):
    template_name = "guitar_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            context["guitars"] = Guitar.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["guitars"] = Guitar.objects.all()
            # default header for not searching 
            context["header"] = "Trending Guitars"
        return context


class GuitarCreate(CreateView):
    model = Guitar
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "guitar_create.html"
    def get_success_url(self):
        return reverse('guitar_detail', kwargs={'pk': self.object.pk})

class GuitarDetail(DetailView):
    model = Guitar
    template_name = "guitar_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        return context


class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "guitar_update.html"
    
    def get_success_url(self):
        return reverse('guitar_detail', kwargs={'pk': self.object.pk})

class GuitarDelete(DeleteView):
    model = Guitar
    template_name = "guitar_delete_confirmation.html"
    success_url = "/guitars/"

class ArtistCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        band = request.POST.get("band")
        guitar = Guitar.objects.get(pk=pk)
        Artist.objects.create(name=name, band=band, guitar=guitar)
        return redirect('guitar_detail', pk=pk)


class GenreArtistAssoc(View):

    def get(self, request, pk, artist_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Genre.objects.get(pk=pk).artists.remove(artist_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Genre.objects.get(pk=pk).artists.add(artist_pk)
        return redirect('home')



