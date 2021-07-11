from django.contrib import admin

from .models import Training
from .models import TrainingCategory
from .models import TrainingSource

# Configure admin settings for Learning app
class TrainingAdmin(admin.ModelAdmin):
    list_per_page = 200
    search_fields = ('title', 'year_published')

class TrainingCategoryAdmin(admin.ModelAdmin):
    list_per_page = 200
    search_fields = ('name', )

class TrainingSourceAdmin(admin.ModelAdmin):
    list_per_page = 200
    search_fields = ('name', )

# Register models
admin.site.register(Training, TrainingAdmin)
admin.site.register(TrainingCategory, TrainingCategoryAdmin)
admin.site.register(TrainingSource, TrainingSourceAdmin)

