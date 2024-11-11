from rest_framework.serializers import ModelSerializer

from .models import Contact
from .validators import validate_phone_number


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
        ]

    def validate_phone_number(self, value):
        validate_phone_number(value)
        return value
