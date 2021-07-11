from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

# Note - if you want to do multiple levels (nested) in URIs, 
# look into drf-nested-routers: https://github.com/alanjds/drf-nested-routers
# Don't have time to mess with it now
# For now, limit to 2 levels, one slash (i.e., "learning/training_sources" not "learning/training/sources")

# Remember to register new ViewSets here for each API endpoint
# Here the string determines the part of the URI path after "api/" (e.g., "api/movies")
router.register(r'movies', views.MovieViewSet)  # represents the URL path after /api
router.register(r'learning/trainings', views.TrainingViewSet)
router.register(r'learning/training_sources', views.TrainingSourceViewSet)
router.register(f'learning/training_categories', views.TrainingCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

