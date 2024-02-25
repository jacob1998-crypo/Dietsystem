# userprofile/urls.py

from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('userprofile/',views.update_profile, name='update_profile'),
    path("recommendations/",views.get_recommendations, name='recommendations'),
]