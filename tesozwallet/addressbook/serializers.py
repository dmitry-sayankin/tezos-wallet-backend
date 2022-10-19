from rest_framework import serializers

from addressbook.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'wallet_address')
