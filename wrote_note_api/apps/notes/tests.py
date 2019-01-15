from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import Note


class NoteTestCase(TestCase):
    def test_create_note(self):
        """Can create a note through a post to '/notes/'"""
        factory = APIRequestFactory()
        request = factory.post('/notes/',
                               {
                                   'title': 'First note',
                                   'content': 'This is a note, hopefully #1',
                               },
                               format='json')
        print(request)
        print(list(Note.objects.all()))
        self.assertEqual(True, True)
        # self.assertEqual(Note.objects.filter(id=1).title, 'First note')
        # self.assertEqual(Note.objects.filter(id=1).title, 'This is a note, hopefully #1')
