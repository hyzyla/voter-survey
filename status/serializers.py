from rest_framework import serializers

from .models import Status, Option
from django.conf import settings
from territory.models import PollingStation
from territory.serializers import PollingStationSerializer

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('value',)


class StatusSerializer(serializers.ModelSerializer):
    is_static = serializers.NullBooleanField(required=False)
    station = PollingStationSerializer(required=False, read_only=True)

    class Meta:
        model = Status
        fields = ('id', 'name', 'type', 'is_static', 'options', 'station')

    options = OptionSerializer(many=True)
    #options = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name') 
    #serializers.StringRelatedField(many=True)

    
    def create(self, validated_data):
        
        options = validated_data.pop('options')
        status = Status.objects.create(**validated_data)
        for option in options:
            Option.objects.create(status=status, **option)
        return status

    def update(self, instance, validated_data):
        from pprint import pprint
        pprint(validated_data)

        options = validated_data.pop('options')
        instance.name = validated_data["name"]
        instance.type = validated_data["type"]
        instance.is_static = validated_data.get("is_static", None)

        if validated_data.get("is_static", None) and instance.stations:
            print("Clearing stations...")
            instance.stations.clear()

        Option.objects.filter(status=instance).delete()
        for option in options:
            Option.objects.create(status=instance, **option)
        instance.save()
        return instance
    #choises = PollingStation.objects.all()[:settings.REST_FRAMEWORK['HTML_SELECT_CUTOFF']]
    #stations = serializers.ManyRelatedField()
