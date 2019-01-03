from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
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


class NoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    Additional actions can be defined individually.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
