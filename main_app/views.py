from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView

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



 #adds artist class for mock database data
class Guitar:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


guitars = [
  Guitar("Fender Stratocaster", "https://i.imgur.com/neHG5h8.jpg",
          "The Fender Stratocaster, colloquially known as the Strat, is a model of electric guitar designed from 1952 into 1954 by Leo Fender, Bill Carson, George Fullerton, and Freddie Tavares. The Fender Musical Instruments Corporation has continuously manufactured the Stratocaster since 1954. It is a double-cutaway guitar, with an extended top horn shape for balance."),
  Guitar("Fender Telecaster",
          "https://i.imgur.com/t6VEt2h.jpg", "The Fender Telecaster, colloquially known as the Tele, is an electric guitar produced by Fender. Together with its sister model the Esquire, it is the world's first mass-produced, commercially successful[note 1] solid-body electric guitar. Its simple yet effective design and revolutionary sound broke ground and set trends in electric guitar manufacturing and popular music."),
  Guitar("Fender Jaguar", "https://i.imgur.com/2wO0zEJ.jpg",
          "The Fender Jaguar is an electric guitar by Fender Musical Instruments characterized by an offset-waist body, a relatively unusual switching system with two separate circuits for lead and rhythm, and a short-scale 24inch neck. Owing some roots to the Jazzmaster, it was introduced in 1962 as Fender's feature-laden top-of-the-line model, designed to lure players from Gibson. "),
  Guitar("Gibson Les Paul",
          "https://i.imgur.com/0IbYBN9.jpg", "The Gibson Les Paul is a solid body electric guitar that was first sold by the Gibson Guitar Corporation in 1952.[1] The guitar was designed by factory manager John Huis and his team with input from and endorsement by guitarist Les Paul. Its typical design features a solid mahogany body with a carved maple top and a single cutaway, a mahogany set-in neck with a rosewood fretboard, two pickups with independent volume and tone controls, and a stoptail bridge, although variants exist."),
  Guitar("Gibson ES-335",
          "https://i.imgur.com/lAhoGOR.jpg", "The Gibson ES-335 is the world's first commercial semi-hollowbody electric guitar, sometimes known as semi-acoustic. Released by the Gibson Guitar Corporation as part of its ES (Electric Spanish) series in 1958, it is neither fully hollow nor fully solid; instead, a solid maple wood block runs through the center of its body. The side wings formed by the two cutaways into its upper bouts are hollow, and the top has two violin-style f-holes over the hollow chambers.[1] Since its release, Gibson has released numerous variations of and other models based on the design of the ES-335."),
  Guitar("Gibson Flying V",
          "https://i.imgur.com/9tj0hZD.jpg", "The Gibson Flying V is an electric guitar model introduced by Gibson in 1958. The Flying V offered a radical, futuristic body design, much like its siblings: the Explorer, which was released the same year, and the Moderne, which was designed in 1957 but not released until 1982. The initial run of guitars used a distinctive wood of the Limba tree marketed by Gibson under the trade name korina; later models used more conventional woods."),
]

class GuitarList(TemplateView):
    template_name = "guitar_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guitars"] = guitars # this is where we add the key into our context object for the view to use
        return context
