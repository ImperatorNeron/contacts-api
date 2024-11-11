from django.urls import path

from . import views

urlpatterns = [
    path('google/', views.google_auth, name='google_auth'),
    path('google/callback/', views.google_callback, name='google_callback'),
]
