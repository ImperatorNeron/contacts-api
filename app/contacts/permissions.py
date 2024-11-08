import requests
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from app.settings import ALLOWED_HOSTS


class RegionRestrictionPermission(permissions.BasePermission):

    ALLOWED_COUNTRIES = ["UA", "PL"]
    API_URL = "https://ipapi.co/{ip}/json/"

    def has_permission(self, request, view):
        user_ip = self.get_client_ip(request=request)
        if not user_ip:
            raise PermissionDenied("Не вдалося визначити ip-адресу")

        if user_ip in ALLOWED_HOSTS:
            return True

        location = self.get_location_data(ip=user_ip)
        if not location:
            raise PermissionDenied("Не вдалося визначити регіон")

        if location.get("country_code") in self.ALLOWED_COUNTRIES:
            return True

        raise PermissionDenied("Дане API заборонене для вашого регіону.")

    def get_client_ip(self, request):
        if x_forwarded_for := request.META.get("HTTP_X_FORWARDED_FOR"):
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")

    def get_location_data(self, ip):
        try:
            response = requests.get(self.API_URL.format(ip=ip))
            if response.status_code == 200:
                return response.json()
        except requests.RequestException as e:
            print(e)
