import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    phone_regex = re.compile(r'^\+?1?\d{9,15}$')
    if not phone_regex.match(value):
        raise ValidationError(
            "Номер телефону має бути у форматі: '+380965557744'. Допускається до 15 цифр.",
        )
