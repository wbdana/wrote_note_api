from ..models import Owner, Collaborator, Reader, Note, Checklist, ChecklistItem


# https://stackoverflow.com/questions/12578908/separation-of-business-logic-and-data-access-in-django/12579490#12579490
def get_notes(limit=None, **filters):
    """Extensible service function for getting notes."""
    if limit:
        return Note.objects.filter(**filters)[:limit]
    return Note.objects.filter(**filters)


def get_owner_notes(owner_id):
    """Gets notes owned by an owner."""
    return get_notes(owner_id=owner_id)
