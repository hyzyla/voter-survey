from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import StatusViewSet, OptionViewSet 

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'statuses', StatusViewSet)
router.register(r'options', OptionViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]