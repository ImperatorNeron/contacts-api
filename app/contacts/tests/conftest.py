import pytest
from contacts.views import ListCreateContactAPIView
from oauth2.permissions import IsAuthenticatedFakePermission


@pytest.fixture(autouse=True)
def set_permission_classes():
    """Fixture that automatically sets fake resolution."""
    original_permission_classes = ListCreateContactAPIView.permission_classes
    ListCreateContactAPIView.permission_classes = [IsAuthenticatedFakePermission]
    yield
    ListCreateContactAPIView.permission_classes = original_permission_classes
