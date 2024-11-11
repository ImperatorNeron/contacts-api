from oauth2.permissions import IsAuthenticatedPermission
from rest_framework import generics, mixins

from .filters import search_contacts
from .models import Contact
from .serializers import ContactSerializer


class ListCreateContactAPIView(
    generics.ListCreateAPIView,
):
    """API view to list and create contacts."""

    permission_classes = [IsAuthenticatedPermission]
    serializer_class = ContactSerializer

    def get_queryset(self):
        """Returns the list of contacts, filtered by the first and/or last
        name."""

        first_name = self.request.GET.get("first_name", None)
        last_name = self.request.GET.get("last_name", None)
        return search_contacts(first_name, last_name)


class DetailUpdateDeleteContactAPIView(
    mixins.UpdateModelMixin,
    generics.RetrieveDestroyAPIView,
):
    """API view to retrieve, update, and delete a specific contact by ID."""

    permission_classes = [IsAuthenticatedPermission]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
