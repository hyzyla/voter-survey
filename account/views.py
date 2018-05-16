# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from voter.models import Voter
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
        user = self.get_object()
        voters_ids = request.data
        voters = Voter.objects.filter(id__in=voters_ids)
        user.voters.set(voters)
        #statuses = StatusSerializer(station.statuses.all(), context={'request': request}, many=True)
        return Response()

    @list_route(methods=['get'], url_path='operators')
    def operators(self, request, pk=None):
        """Оператори """
        operator_group = None
        for group in Group.objects.all():
            if 'оператор' in group.name.lower():
                operator_group = group
                
        if operator_group:  
            operators = User.objects.filter(groups=operator_group)
        else:
            operators = []
        return Response(UserSerializer(operators, many=True).data)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування груп.
    """

    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


