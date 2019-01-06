from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import OwnerViewSet, CollaboratorViewSet, ReaderViewSet, NoteViewSet, UserViewSet, ChecklistViewSet,\
    ChecklistItemViewSet

schema_view = get_schema_view(title='Notes API')

# Create a router and register our viewsets with it.
router = DefaultRouter()  # Automatically creates the root '/' view
router.register(r'owners', OwnerViewSet)
router.register(r'collaborators', CollaboratorViewSet)
router.register(r'readers', ReaderViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'users', UserViewSet)
router.register(r'checklists', ChecklistViewSet)
router.register(r'checklistitems', ChecklistItemViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls))
]
