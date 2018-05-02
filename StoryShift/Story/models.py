from django.db import models
from django.urls import reverse

# Create your models here.

class Story(models.Model):
    name = models.CharField(max_length=200, help_text="Enter AU's Name")
    logoFileName = models.CharField(max_length=200, null = True ,help_text="Enter Image Location")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('storyDetail' , args=[str(self.id)])

class Location(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Location Name")
    story = models.ForeignKey('Story', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('locationDetail' , args=[str(self.id)])

class Characters(models.Model):
    name = models.CharField(max_length=200, help_text="Enter NPC's Name")
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    story = models.ForeignKey('Story', on_delete=models.SET_NULL, null=True)
    imageFileName = models.CharField(max_length=200, help_text="Enter logo file name", null=True)

class LocationNeighbors(models.Model):
    fromLocation = models.ForeignKey('Location' , on_delete=models.SET_NULL , null=True , related_name='fromLocation')
    toLocation = models.ForeignKey('Location' , on_delete=models.SET_NULL , null=True , related_name='toLocation')

    CARDINAL = (
        ('n' , 'North'),
        ('s' , 'South'),
        ('e' , 'East'),
        ('w' , 'West'),
    )

    direction = models.CharField(max_length=2 , choices=CARDINAL , help_text="Select a Driection" , null=True , blank=True)

    #def __str__(self):
        #return str(self.fromLocation) + ': ' + str(self.direction) + 'to: ' + str(self.toLocation)