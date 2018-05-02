from django.shortcuts import render

# Create your views here.

def index(request):
    temporaryData = "Asriel"
    return render(
        request,
	"index.html",
	context = {'temporaryData':temporaryData,},
    )

from django.views import generic


from .models import Story , Location , Characters

class StoryListView(generic.ListView):
    model = Story
    paginate_by = 10

class StoryDetailView(generic.DetailView):
    model = Story

class LocationDetailView(generic.DetailView):
    model = Location

class CharacterDetailView(generic.DetailView):
    model = Characters