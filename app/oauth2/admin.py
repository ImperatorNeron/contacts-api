from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "google_id", "name", "email")
    list_display_links = ("pk", "google_id", "name", "email")
    readonly_fields = ("google_id", "name", "email")
