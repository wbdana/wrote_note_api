# Generated by Django 2.1.4 on 2019-01-08 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20190108_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistitem',
            name='checklist',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='checklists', to='notes.Checklist'),
        ),
    ]