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

    def filter(self, queryset, user):
        return queryset.filter(operators=user)

    def list(self, request, *args, **kwargs):
        user = request.user

        operator = None
        for group in Group.objects.all():
            if 'оператор' in group.name.lower():
                operator = group

        queryset = self.get_queryset()
        if operator in user.groups.all():
            queryset = self.filter(queryset, user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        voter_id = response.data['id']
        voter = Voter.objects.get(id=voter_id)
        voter.operators.add(request.user)
        return response