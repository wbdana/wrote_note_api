# Generated by Django 2.1.4 on 2019-01-08 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20190106_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='reader',
            new_name='readers',
        ),
    ]
