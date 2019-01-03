from rest_framework import serializers
from .models import Note, Checklist, ChecklistItem
from django.contrib.auth.models import User


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ('url', 'id', 'owner', 'title', 'content',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(many=True, view_name='note-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'notes',)


class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    # TODO WBD should view_name here be 'checklistitem-detail'?
    checklist_items = serializers.HyperlinkedRelatedField(many=True, view_name='checklist-item-detail', read_only=True)
    note_id = serializers.HyperlinkedRelatedField(many=False, view_name='note-detail', read_only=True)

    class Meta:
        model = Checklist
        fields = ('url', 'id', 'checklist_items', 'note_id',)


class ChecklistItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChecklistItem
        fields = ('url', 'id', 'content', 'checklist_id',)
