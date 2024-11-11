import pytest
from rest_framework import status
from rest_framework.test import APIClient

from .contacts_factory import ContactModelFactory


@pytest.mark.django_db
@pytest.mark.parametrize(
    "ip, expected_status",
    [
        ("185.68.16.1", status.HTTP_200_OK),  # Uk
        ("103.68.134.5", status.HTTP_200_OK),  # Pl
        ("15.135.30.20", status.HTTP_403_FORBIDDEN),
    ],
)
def test_get_region_allow(client: APIClient, ip, expected_status):
    """Test checks access to data based on IP address."""
    url = "http://localhost:8000/api/contacts/"
    headers = {"X-Forwarded-For": ip}

    response = client.get(url, headers=headers)
    assert response.status_code == expected_status


@pytest.mark.django_db
def test_create_duplicate(client: APIClient):
    """Tests the creation of the same contact twice."""
    url = "http://localhost:8000/api/contacts/"

    data = ContactModelFactory.build().__dict__
    data.pop("_state", None)
    data.pop("id", None)

    response = client.post(url, data=data)
    assert response.status_code == status.HTTP_201_CREATED
    response = client.post(url, data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in response.data
    assert "phone_number" in response.data


@pytest.mark.django_db
def test_filters(client: APIClient):
    """Tests the filtering of contacts by first_name and/or last_name."""
    url = "http://localhost:8000/api/contacts/"

    ContactModelFactory.create(first_name="John", last_name="Doe")
    ContactModelFactory.create(first_name="Jane", last_name="Doe")
    ContactModelFactory.create(first_name="John", last_name="Smith")

    response = client.get(url, {"first_name": "John"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

    response = client.get(url, {"last_name": "Doe"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

    response = client.get(url, {"first_name": "John", "last_name": "Doe"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3

    response = client.get(url, {"first_name": "Alice"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0
