from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Owner, Collaborator, Reader, Note, Checklist, ChecklistItem
from .serializers import OwnerSerializer, CollaboratorSerializer, ReaderSerializer, NoteSerializer, UserSerializer, ChecklistSerializer, ChecklistItemSerializer
from .permissions import IsNoteOwnerOrReadOnly, IsChecklistOwnerOrReadOnly
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format),
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    Additional actions can be defined individually.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsNoteOwnerOrReadOnly,
    )


class ChecklistViewSet(viewsets.ModelViewSet):
    """
    Provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for Checklist.
    """
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsChecklistOwnerOrReadOnly
    )


class ChecklistItemViewSet(viewsets.ModelViewSet):
    """
    Provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for ChecklistItem.
    """
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
