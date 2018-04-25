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


from .models import Story

class StoryListView(generic.ListView):
    model = Story
    paginate_by = 10