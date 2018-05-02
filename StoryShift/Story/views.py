from django.shortcuts import render
from django.views import generic

# Create your views here.

def aboutus(request):
    return render(
        request,
	"zoo/aboutus.html",
	context = { },
    )


from .models import Story , Location , Characters

class StoryListView(generic.ListView):
    model = Story

class StoryDetailView(generic.DetailView):
    model = Story

class LocationDetailView(generic.DetailView):
    model = Location

class CharacterDetailView(generic.DetailView):
    model = Characters