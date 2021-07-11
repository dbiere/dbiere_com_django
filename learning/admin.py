from django.contrib import admin

from .models import Training
from .models import TrainingCategory
from .models import TrainingSource

# Configure admin settings for Learning app
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'trainer', 'category', 'date_started', 'is_complete']
    list_display_links = ['title', ]
    list_editable = ('is_complete',)
    list_filter = ('is_complete', 'source', 'category', 'date_started')
    list_per_page = 200
    ordering = ('-date_started',)
    search_fields = ('title', 'year_published')
    
class TrainingCategoryAdmin(admin.ModelAdmin):
    list_per_page = 200
    ordering = ('name', )
    search_fields = ('name', )
    
class TrainingSourceAdmin(admin.ModelAdmin):
    list_per_page = 200
    ordering = ('name',)
    search_fields = ('name', )

# Register models
admin.site.register(Training, TrainingAdmin)
admin.site.register(TrainingCategory, TrainingCategoryAdmin)
admin.site.register(TrainingSource, TrainingSourceAdmin)

