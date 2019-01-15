from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Owner, Collaborator, Reader, Note, Checklist, ChecklistItem
from .serializers import OwnerSerializer, CollaboratorSerializer, ReaderSerializer, NoteSerializer, UserSerializer,\
    ChecklistSerializer, ChecklistItemSerializer
from .permissions import IsNoteOwnerOrReadOnly, IsChecklistOwnerOrReadOnly
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from rest_framework.response import Response
# Token authentication
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format),
    })


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


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

    @action(detail=True, methods=["GET", "POST"])
    def checklists(self, request, pk=None):
        note = self.get_object()
        checklists = Checklist.objects.filter(note_id=note.id)
        context = {
            'request': request,
        }
        serializer = ChecklistSerializer(checklists, many=True, context=context)
        return Response(serializer.data, status=200)


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

    @action(detail=True, methods=["GET", "POST"])
    def checklist_items(self, request, pk=None):
        checklist = self.get_object()
        checklist_items = ChecklistItem.objects.filter(checklist_id=checklist.id)
        context = {
            'request': request,
        }
        serializer = ChecklistSerializer(checklist_items, many=True, context=context)
        return Response(serializer.data, status=200)


class ChecklistItemViewSet(viewsets.ModelViewSet):
    """
    Provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for ChecklistItem.
    """
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
