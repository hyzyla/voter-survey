from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import VoterViewSet

# Create a router and register our viewsets with it.
router = SimpleRouter()
#router.register(r'records', RecordViewSet)
router.register(r'voters', VoterViewSet)
#router.register(r'rows', RecordsList, base_name="rows-list")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    #path('rows',  RecordsList.as_view({'get': 'list'}), name='rows')
]
