from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


@receiver(post_save, sender=User)
def create_user_roles(sender, instance, created, **kwargs):
    """
    Creates an associated owner, collaborator, and reader profile (role) for each User.
    :param sender: User model
    :param instance: User instance
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Owner.objects.create(user=instance)
        Collaborator.objects.create(user=instance)
        Reader.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_roles(sender, instance, **kwargs):
    """
    Updates associated owner, collaborator, and reader roles for each User when User is saved.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.owner.save()
    instance.collaborator.save()
    instance.reader.save()


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE, default='1')
    collaborator = models.ForeignKey

    class Meta:
        ordering = ('created',)


class NoteUser(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
