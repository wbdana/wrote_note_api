from rest_framework import serializers
from .models import Owner, Collaborator, Reader, Note, Checklist, ChecklistItem
from django.contrib.auth.models import User


class ChecklistItemSerializer(serializers.HyperlinkedModelSerializer):
    checklist = serializers.HyperlinkedRelatedField(many=False, view_name='checklist-detail', read_only=True)

    class Meta:
        model = ChecklistItem
        fields = ('url', 'id', 'content', 'checklist',)


class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    checklists = ChecklistItemSerializer(many=True, read_only=True)
    note = serializers.HyperlinkedRelatedField(many=False, view_name='note-detail', read_only=True)

    class Meta:
        model = Checklist
        fields = ('url', 'id', 'checklists', 'note',)


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)
    checklists = ChecklistSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ('url', 'id', 'owner', 'title', 'content', 'checklists',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # notes = serializers.HyperlinkedRelatedField(many=True, view_name='note-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username',)


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('url', 'id', 'user', 'notes', )


class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Collaborator
        fields = ('url', 'id', 'user', 'notes',)


class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = ('url', 'id', 'user', 'notes',)

