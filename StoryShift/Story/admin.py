from django.contrib import admin

# Register your models here.

from .models import Story, Location, Characters, LocationNeighbors

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'logoFileName')

admin.site.register(Story, StoryAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'story')

admin.site.register(Location, LocationAdmin)

class CharactersAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'story' , 'imageFileName' , 'dialougueOne' , 'answerOne' ,'dialougueTwo' , 'dialougueThree')
	# location , get_absolute_url

admin.site.register(Characters, CharactersAdmin)

class LocationNeighborsAdmin(admin.ModelAdmin):
    list_display = ('fromLocation' , 'direction' , 'toLocation')

admin.site.register(LocationNeighbors, LocationNeighborsAdmin)