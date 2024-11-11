import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_cannot_get_data_without_login(client: APIClient):
    """Access to data without authentication is denied."""

    url = "http://localhost:8000/api/contacts/"
    headers = {"X-Forwarded-For": "185.68.16.1"}  # Right ip

    response = client.get(url, headers=headers)
    assert response.status_code == status.HTTP_403_FORBIDDEN
