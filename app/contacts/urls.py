from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListCreateContactAPIView.as_view(), name="list_contacts"),
    path(
        "<int:pk>/",
        views.DetailUpdateDeleteContactAPIView.as_view(),
        name="detail_contact",
    ),
]
