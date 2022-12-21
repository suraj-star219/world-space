from django.urls import path, include
from .views import *
from Profile import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Profile', views.UserProfileViewSet,basename="Profile")
# router.register(r'Profile/<int:id>', views.UserProfileViewSet,basename="Profile")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]