from django.db.models import Q

from .models import Contact


def search_contacts(first_name: str | None = None, last_name: str | None = None):
    """Find contacts by searching for their name or/and surname."""

    query = Q()
    if first_name:
        query |= Q(first_name__icontains=first_name.capitalize())
        query |= Q(first_name__icontains=first_name)

    if last_name:
        query |= Q(last_name__icontains=last_name.capitalize())
        query |= Q(last_name__icontains=last_name)

    if query:
        return Contact.objects.filter(query)

    return Contact.objects.all()
