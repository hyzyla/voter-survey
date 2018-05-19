# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .models import Region, District, Constituency, PollingStation
from .serializers import RegionSerializer, DistrictSerializer, ConstituencySerializer, PollingStationSerializer
from django.core.exceptions import ObjectDoesNotExist
from status.serializers import StatusSerializer
from status.models import Status
from voter.serializers import VoterSerializer
from voter.models import Voter

class RegionViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування областей.
    """

    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    @detail_route()
    def districts(self, request, pk=None):
        """Список районів даної області"""
        region = self.get_object()
        serializer = DistrictSerializer(region.districts.all(), context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route()
    def constituencies(self, request, pk=None):
        """Список округів даної області"""
        region = self.get_object()
        serializer = DistrictSerializer(region.constituencies.all(), context={'request': request}, many=True)
        return Response(serializer.data)


    @detail_route(methods=['post'], url_path='add-status')
    def     (self, request, pk=None):
        """Додати статус до всіх дільниць даної області"""
        region = self.get_object()
        status = Status.objects.get(pk=request.data['id'])
        
        # Робимо статус не статичним, оскільки хоча б одна дільниця міститеме даний статус
        status.is_static = False
        stations = PollingStation.objects.filter(district__region=region)
        status.stations.add(*stations)
        status.save()

        return Response()

    @detail_route(methods=['delete'], url_path='statuses')
    def delete_statuses(self, request, pk=None):
        """Видалити всі статуси з кожної дільниці даної області"""
        region = self.get_object()
        stations = PollingStation.objects.filter(district__region=region)
        for station in stations:
            station.statuses.clear()
        return Response()

class DistrictViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування районів.
    """

    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    @detail_route()
    def stations(self, request, pk=None):
        """Список дільниць даного району"""
        district = self.get_object()
        serializer = PollingStationSerializer(district.stations.all(), context={'request': request}, many=True)
        return Response(serializer.data)


    @detail_route(methods=['post'], url_path='add-status')
    def add_status(self, request, pk=None):
        """Додає статус до даного району"""
        district = self.get_object()
        status = Status.objects.get(pk=request.data['id'])

        status.is_static = False
        stations = PollingStation.objects.filter(district=district)
        status.stations.add(*stations)
        status.save()
        return Response()

    @detail_route(methods=['get'], url_path='region')
    def region(self, request, pk=None):
        """Область даного району"""
        district = self.get_object()
        region = RegionSerializer(district.region, context={'request': request})
        return Response(region.data)

    @detail_route(methods=['delete'], url_path='statuses')
    def delete_statuses(self, request, pk=None):
        """Видалити всі статуси кожної дільниці даного району """
        district = self.get_object()
        stations = PollingStation.objects.filter(district=district)
        for station in stations:
            station.statuses.clear()
        return Response()

class ConstituencyViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування виборчих округів.
    Виборчий округ не є точним відображенням вибочого округу, 
    це просто список виборчих дільниць визначений користувачем
    """

    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    queryset = Constituency.objects.all()
    serializer_class = ConstituencySerializer


    @detail_route()
    def voters(self, request, pk=None):
        """
        Всі виборці даного округу
        """
        constituency = self.get_object()
        voters = Voter.objects.filter(station__constituencies=constituency).distinct()
        serializer = VoterSerializer(voters, context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route()
    def statuses(self, request, pk=None):
        """
        Всі виборці даного округу
        """
        constituency = self.get_object()
        statuses = Status.objects.filter(stations__constituencies=constituency).distinct()
        serializer = StatusSerializer(statuses, context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route()
    def stations(self, request, pk=None):
        """
        Всі дільниці даного округу
        """
        constituency = self.get_object()
        serializer = PollingStationSerializer(constituency.stations.all(), context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route(methods=['put'], url_path='add-region')
    def add_region(self, request, pk=None):
        """
        Додати всі дільниці регіону до округу
        """
        constituency = self.get_object()
        stations = PollingStation.objects.filter(district__region__pk=request.data['id'])
        constituency.stations.add(*stations)
        return Response()

    @detail_route(methods=['put'], url_path='add-district')
    def add_district(self, request, pk=None):
        """
        Додати всі дільниці району до округу
        """
        constituency = self.get_object()
        stations = PollingStation.objects.filter(district__pk=request.data['id'])
        constituency.stations.add(*stations)
        return Response()

    @detail_route(methods=['put'], url_path='add-station')
    def add_station(self, request, pk=None):
        """
        Додати дільницю до округу
        """
        constituency = self.get_object()
        station = PollingStation.objects.get(pk=request.data['id'])
        constituency.stations.add(station)
        return Response()

    @detail_route(methods=['put'], url_path='delete-station')
    def delete_station(self, request, pk=None):
        """"
        Видалити дільницю з округу
        """
        constituency = self.get_object()
        try:
            station = PollingStation.objects.get(pk=request.data['id'])
        except ObjectDoesNotExist:
            return Response()
        
        constituency.stations.remove(station)
        return Response()


class PollingStationViewSet(viewsets.ModelViewSet):
    """
    API для відображення і редагування виборчих дільниць.
    """

    permission_classes = (IsAuthenticated, DjangoModelPermissions, )
    queryset = PollingStation.objects.all()
    serializer_class = PollingStationSerializer
    
    @detail_route(methods=['get'], url_path='statuses')
    def show_status(self, request, pk=None):
        """Всі статуси для даної дільниці"""
        station = self.get_object()
        statuses = StatusSerializer(station.statuses.all(), context={'request': request}, many=True)
        return Response(statuses.data)

    @detail_route(methods=['get'], url_path='voter-number')
    def voter_number(self, request, pk=None):
        """Повернути кількість виборців у даній дільниці"""
        station = self.get_object()
        return Response(station.voter_set.count())

    @detail_route(methods=['post'], url_path='create-records')
    def create_records(self, request, pk=None):
        station = self.get_object()
        amount = int(request.data)
        station.voter_set.bulk_create([Voter(station=station) for i in range(amount)])
        station.save()
        return Response()


    @detail_route(methods=['delete'], url_path='delete-statuses')
    def delete_statuses(self, request, pk=None):
        """Видалити всі статуси, що пов'язані з даною дільницею"""
        station = self.get_object()
        if station.statuses:
            station.statuses.clear()
        return Response()
    

    @detail_route(methods=['post'], url_path='add-status')
    def add_status(self, request, pk=None):
        """Додати статус до дільниці"""
        station = self.get_object()
        status = Status.objects.get(pk=request.data['id'])
        status.is_static = False
        status.save()
        station.statuses.add(status)
        station.save()
        return Response()

    @detail_route(methods=['put'], url_path='delete-status')
    def delete_status(self, request, pk=None):
        """Видалити стутус з дільниці"""
        station = self.get_object()
        try:
            status = Status.objects.get(pk=request.data['id'])
        except ObjectDoesNotExist:
            return Response()
        
        station.statuses.remove(status)
        station.save()
        return Response()
    
    @detail_route(methods=['get'], url_path='district')
    def district(self, request, pk=None):
        """Район даної дільниці"""
        station = self.get_object()
        district = DistrictSerializer(station.district, context={'request': request})
        return Response(district.data)