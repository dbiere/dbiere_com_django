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
