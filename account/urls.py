from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import GroupViewSet, UserViewSet

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]