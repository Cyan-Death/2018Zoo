from django.db import models

# Create your models here.

class Story(models.Model):
    name = models.CharField(max_length=200, help_text="Enter AU's Name")
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Location Name")
    story = models.ForeignKey('Story', on_delete=models.SET_NULL, null=True)