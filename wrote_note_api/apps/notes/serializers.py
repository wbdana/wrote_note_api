from rest_framework import serializers
from .models import Note
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
