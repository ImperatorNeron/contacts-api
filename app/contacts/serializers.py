from rest_framework.serializers import ModelSerializer, ValidationError

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

        if Contact.objects.filter(phone_number=value).exists():
            raise ValidationError("Цей номер телефону вже зареєстровано.")

        return value

    def validate_email(self, value):
        if Contact.objects.filter(email=value).exists():
            raise ValidationError("Ця електронна пошта вже використовується.")
        return value
