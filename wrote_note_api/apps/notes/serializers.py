from rest_framework import serializers
from .models import Owner, Collaborator, Reader, Note, Checklist, ChecklistItem
from django.contrib.auth.models import User


class ChecklistItemSerializer(serializers.HyperlinkedModelSerializer):
    checklist = serializers.HyperlinkedRelatedField(many=False, view_name='checklist-detail',
                                                    queryset=Checklist.objects.all())

    class Meta:
        model = ChecklistItem
        fields = ('url', 'id', 'content', 'checklist', 'done',)


class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    checklist_items = ChecklistItemSerializer(many=True, read_only=True)
    note = serializers.HyperlinkedRelatedField(many=False, view_name='note-detail', read_only=True)

    class Meta:
        model = Checklist
        fields = ('url', 'id', 'checklist_items', 'note',)
        depth = 1

    def create(self, validated_data):
        checklist_items_data = validated_data.pop('checklist_items')
        checklist = Checklist.objects.create(**validated_data)
        for checklist_item_data in checklist_items_data:
            ChecklistItem.objects.create(checklist=checklist, **checklist_item_data)
        return checklist


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)
    checklists = ChecklistSerializer(many=True, required=False, read_only=True)  # TODO Check to see what required=False did

    class Meta:
        model = Note
        fields = ('url', 'id', 'owner', 'title', 'content', 'checklists',)

    def create(self, validated_data):
        checklists_data = validated_data.pop('checklists')
        note = Note.objects.create(**validated_data)
        for checklist_data in checklists_data:
            Checklist.objects.create(note=note, **checklist_data)
        return note


class UserSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)
    collaborator = serializers.HyperlinkedRelatedField(many=False, view_name='collaborator-detail', read_only=True)
    reader = serializers.HyperlinkedRelatedField(many=False, view_name='reader-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'owner', 'collaborator', 'reader',)


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

