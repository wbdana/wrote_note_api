from rest_framework import serializers
from .models import Note, Checklist, ChecklistItem
from django.contrib.auth.models import User


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    checklists = serializers.HyperlinkedRelatedField(many=True, view_name='checklist-detail', read_only=True)

    class Meta:
        model = Note
        fields = ('url', 'id', 'owner', 'title', 'content', 'checklists',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(many=True, view_name='note-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'notes',)


class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    checklist_items = serializers.HyperlinkedRelatedField(many=True, view_name='checklistitem-detail', read_only=True)
    note = serializers.HyperlinkedRelatedField(many=False, view_name='note-detail', read_only=True)

    class Meta:
        model = Checklist
        fields = ('url', 'id', 'checklist_items', 'note',)


class ChecklistItemSerializer(serializers.HyperlinkedModelSerializer):
    checklist = serializers.HyperlinkedRelatedField(many=False, view_name='checklist-detail', read_only=True)

    class Meta:
        model = ChecklistItem
        fields = ('url', 'id', 'content', 'checklist',)
