from django.urls import path
from .views import UniversityListAPI, UniversityDetailAPI

urlpatterns = [
    path('apply/', UniversityListAPI.as_view()),
    path('apply/<int:id>/', UniversityDetailAPI.as_view()),
]