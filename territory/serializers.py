from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Region, District, Constituency, PollingStation


class RegionSerializer(serializers.ModelSerializer):
    districts = serializers.HyperlinkedIdentityField(view_name='region-districts')
    constituencies = serializers.HyperlinkedIdentityField(view_name='region-constituencies')

    class Meta:
        model = Region
        fields = ('id', 'name', 'districts', 'constituencies')


class DistrictSerializer(serializers.ModelSerializer):
    stations = serializers.HyperlinkedIdentityField(view_name='district-stations')
    class Meta:
        model = District
        fields = ('id', 'region', 'name', 'city', 'stations')


class ConstituencySerializer(serializers.ModelSerializer):
    stations = serializers.HyperlinkedIdentityField(view_name='constituency-stations')
    class Meta:
        model = Constituency
        fields = '__all__'


class PollingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingStation
        fields = ('id', 'district', 'number', 'description', 'address')

    def to_internal_value(self, data):
        if data.get('id'):
            return get_object_or_404(PollingStation.objects.all(), pk=data.get('id'))
        return super(PollingStationSerializer, self).to_internal_value(data)
