from urllib.parse import urlencode

import requests
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status

from app.settings import env

from .models import UserProfile


def google_auth(request):
    """Initializing authorization through Google."""
    client_id = env("GOOGLE_CLIENT_ID")
    redirect_uri = "http://localhost:8000/auth/google/callback/"
    scope = env("GOOGLE_SCOPE")
    auth_url = "https://accounts.google.com/o/oauth2/auth?" + urlencode(
        {
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "scope": scope,
        },
    )
    return redirect(auth_url)


def google_callback(request):
    """Processing callback after authorization through Google."""

    code = request.GET.get("code")
    client_id = env("GOOGLE_CLIENT_ID")
    client_secret = env("GOOGLE_CLIENT_SECRET")
    redirect_uri = "http://localhost:8000/auth/google/callback/"

    # Exchange code for access_token
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    token_response = requests.post(token_url, data=token_data)
    token_json = token_response.json()
    access_token = token_json.get("access_token")

    # Retrieve user information.
    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    user_info_params = {"access_token": access_token}
    user_info_response = requests.get(user_info_url, params=user_info_params)
    user_info = user_info_response.json()

    if "id" in user_info:
        google_id = user_info["id"]
        name = user_info.get("name")
        email = user_info.get("email")

        # Get or add current user
        user, _ = UserProfile.objects.get_or_create(
            google_id=google_id, defaults={"name": name, "email": email},
        )

        # Save user ID in session for further authentication
        request.session["user_id"] = user.id
        return redirect("list_contacts")

    return JsonResponse(
        {"error": "Unable to retrieve user data"},
        status=status.HTTP_400_BAD_REQUEST,
    )
