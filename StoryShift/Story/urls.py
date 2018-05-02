from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>' , views.StoryDetailView.as_view(), name = 'storyDetail'),
    path('location/<int:pk>' , views.LocationDetailView.as_view(), name = 'locationDetail'),
    path('character/<int:pk>' , views.CharacterDetailView.as_view(), name = 'characterDetail'),
]