from .models import Voter
from rest_framework import serializers
from territory.serializers import PollingStationSerializer

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'

    attrib = serializers.DictField(child=serializers.CharField())
    station = PollingStationSerializer(required=False)
    """
    def validate_attrib(self, value):
        print(value)
        return {"a": "b "}
    """