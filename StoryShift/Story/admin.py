from django.contrib import admin

# Register your models here.

from .models import Story, Location

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')

admin.site.register(Story, StoryAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')

admin.site.register(Location, LocationAdmin)