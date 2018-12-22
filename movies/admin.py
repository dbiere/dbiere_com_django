from django.contrib import admin

from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'year_released', 'is_favorite',)
    list_editable = ('is_favorite',)
    list_filter = ('is_favorite', 'year_released',)
    list_per_page=200
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Movie, MovieAdmin)


'''
from django.contrib import admin

from .models import Listing

# This lets us add filters, etc. to main Listing admin page
# Important: remember to add this to the model registration below if you do this
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

# Register models
admin.site.register(Listing, ListingAdmin)

'''