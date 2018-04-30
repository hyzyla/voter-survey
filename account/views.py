# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class UserViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування користувачів системи .
    """

    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['post'], url_path='assign-voters')
    def assign_voters(self, request, pk=None):
        """Всі статуси для даної дільниці"""
        user = self.get_object()
        
        #statuses = StatusSerializer(station.statuses.all(), context={'request': request}, many=True)
        return Response()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування груп.
    """

    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


