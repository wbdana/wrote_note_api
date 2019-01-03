from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import NoteViewSet, UserViewSet

schema_view = get_schema_view(title='Notes API')

# Create a router and register our viewsets with it.
router = DefaultRouter()  # Automatically creates the root '/' view
router.register(r'notes', NoteViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls))
]
