from django.contrib import admin

from .models import Author
from .models import Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_per_page = 200
    search_fields = ('display_name',)
    

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_authors')
    list_filter = ('author__formal_sort_name',)
    list_per_page = 200
    ordering = ('title',)
    search_fields = ('title', 'author__display_name')

    # Have to do this to show many-to-many objects
    def show_authors(self, obj):
        return ", ".join([a.formal_sort_name for a in obj.author.all()])
    
    show_authors.short_description = 'Author(s)'

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
