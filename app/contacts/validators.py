import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    """Validates that the phone number starts with '+' followed by 9 to 15
    digits."""

    phone_regex = re.compile(r"^\+\d{9,15}$")

    if not phone_regex.match(value):
        raise ValidationError(
            "The phone number should be in the format: '+380965557744'. Up to 15 digits are allowed.",
        )
