from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/contacts/", include("contacts.urls")),
    path("auth/", include("oauth2.urls")),
]
