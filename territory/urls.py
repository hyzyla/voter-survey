from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import RegionViewSet, DistrictViewSet, ConstituencyViewSet, PollingStationViewSet

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'regions', RegionViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'constituencies', ConstituencyViewSet)
router.register(r'polling-stations', PollingStationViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]