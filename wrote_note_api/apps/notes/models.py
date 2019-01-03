from django.db import models


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE, default='1')

    class Meta:
        ordering = ('created',)


class Checklist(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey('Note', related_name='note', on_delete=models.CASCADE, default='1')

    class Meta:
        ordering = ('created',)


class ChecklistItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    checklist = models.ForeignKey('Checklist', related_name='checklist_items', on_delete=models.CASCADE, default='1')

    class Meta:
        ordering = ('created',)
