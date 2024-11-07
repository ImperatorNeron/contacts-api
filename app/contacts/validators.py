import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    phone_regex = re.compile(r'^\+?1?\d{9,15}$')
    if not phone_regex.match(value):
        raise ValidationError(
            "The phone number must be in the format: '+380965557744'. Up to 15 digits are allowed.",
        )
