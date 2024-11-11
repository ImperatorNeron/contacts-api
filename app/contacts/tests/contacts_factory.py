import random

import factory
from contacts.models import Contact
from faker import Faker

fake = Faker()


class ContactModelFactory(factory.Factory):
    """Factory for creating fake data for Contact."""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    phone_number = factory.LazyAttribute(
        lambda _: f"+{str(random.SystemRandom().randint(1000000000, 9999999999))}",
    )
    email = factory.Faker("email")

    class Meta:
        model = Contact
