# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування користувачів системи .
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування груп.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


