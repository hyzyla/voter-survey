# Create your views here.
from .models import Status, Option
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .serializers import StatusSerializer, OptionSerializer

class StatusViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування статусів (атрибутів виборця).
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    @list_route(methods=['GET'], url_path='static')
    def static(self, request, pk=None):
        serializer = StatusSerializer(Status.objects.filter(is_static=True), context={'request': request}, many=True)
        return Response(serializer.data)

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer