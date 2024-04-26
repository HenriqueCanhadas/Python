from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('home/', homepage),
]