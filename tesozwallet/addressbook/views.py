from rest_framework import viewsets

from addressbook.serializers import ContactSerializer
from addressbook.models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
