# Generated by Django 2.1.4 on 2019-01-06 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20190106_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noteuser',
            name='note',
        ),
        migrations.RemoveField(
            model_name='noteuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='NoteUser',
        ),
    ]
