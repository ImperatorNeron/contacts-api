import requests
from django.http import JsonResponse
from rest_framework import status

from app.settings import ALLOWED_HOSTS


class CountryRestrictionMiddleware:
    """Middleware, which restricts access to the API by geolocation of the
    user."""

    ALLOWED_COUNTRIES = ["UA", "PL"]
    API_URL = "https://ipapi.co/{ip}/json/"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = self.get_client_ip(request=request)
        # Check the availability of IP and access permission
        if not user_ip:
            return JsonResponse(
                {"error": "Unable to determine IP address"},
                status=status.HTTP_403_FORBIDDEN,
            )
        if user_ip in ALLOWED_HOSTS:
            return self.get_response(request)

        # Get current user location
        location = self.get_location_data(ip=user_ip)
        if not location:
            return JsonResponse(
                {"error": "Unable to determine region"},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Check if the country is allowed
        if location.get("country_code") not in self.ALLOWED_COUNTRIES:
            return JsonResponse(
                {"error": "This API is not allowed for your region."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return self.get_response(request)

    def get_client_ip(self, request):
        """Returns the IP address from the'X-Forwarded-For 'or' REMOTE_ADDR
        header."""

        if x_forwarded_for := request.META.get("HTTP_X_FORWARDED_FOR"):
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")

    def get_location_data(self, ip):
        """Receives location data over IP via API."""

        try:
            response = requests.get(self.API_URL.format(ip=ip))
            if response.status_code == 200:
                return response.json()
        except requests.RequestException as e:
            print(e)
