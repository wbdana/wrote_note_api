from django.contrib import admin
from .models import Owner, Collaborator, Reader, Note, Checklist, ChecklistItem

# Register your models here.
admin.site.register(Owner)
admin.site.register(Collaborator)
admin.site.register(Reader)
admin.site.register(Note)
admin.site.register(Checklist)
admin.site.register(ChecklistItem)
