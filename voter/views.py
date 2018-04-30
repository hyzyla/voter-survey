from rest_framework import viewsets
from .models import Voter
from .serializers import VoterSerializer
from rest_framework.response import Response
#from django_mysql.models import field 
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.contrib.auth.models import Group

class VoterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer



    def filter_queryset(self, queryset, user):
        return queryset.filter(operators=user)

    def list(self, request, *args, **kwargs):
        user = request.user
        operator = Group.objects.all()[3]

        queryset = self.get_queryset()
        if operator in user.groups.all():
            queryset = self.filter_queryset(queryset, user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)