from rest_framework import viewsets
from .models import Voter
from .serializers import VoterSerializer


class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer