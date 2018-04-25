from django.db import models

# Create your models here.

class Story(models.Model):
    name = models.CharField(max_length=200, help_text="Enter AU's Name")
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Location Name")
    story = models.ForeignKey('Story', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Characters(models.Model):
    name = models.CharField(max_length=200, help_text="Enter NPC's Name")
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)

class LocationNeighbors(models.Model):
    fromLocation = models.ForeignKey('Location' , on_delete=models.SET_NULL , null=True)
    direction = models.CharField(max_length=200)
    toLocation = models.ForeignKey('Location' , on_delete=models.SET_NULL , null=True , related_name='neighbors_of')

    def __str__(self):
        return str(self.fromLocation) + ': ' + str(self.direction) + 'to: ' + str(self.toLocation)