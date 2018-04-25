from django.contrib import admin

# Register your models here.

from .models import Story, Location, Characters, LocationNeighbors

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')

admin.site.register(Story, StoryAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')

admin.site.register(Location, LocationAdmin)

class CharactersAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')

admin.site.register(Characters, CharactersAdmin)

class LocationNeighborsAdmin(admin.ModelAdmin):
    list_display = ('fromLocation' , 'direction' , 'toLocation')

admin.site.register(LocationNeighbors, LocationNeighborsAdmin)