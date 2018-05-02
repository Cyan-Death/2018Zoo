from django.urls import path

from . import views


urlpatterns = [
    path('', views.StoryListView.as_view(), name='storyList'),
    path('<int:pk>' , views.StoryDetailView.as_view(), name = 'storyDetail'),
    path('location/<int:pk>' , views.LocationDetailView.as_view(), name = 'locationDetail'),
    path('character/<int:pk>' , views.CharacterDetailView.as_view(), name = 'characterDetail'),
    path('aboutus/<int:pk>' , views.aboutus, name = 'aboutus'),
]