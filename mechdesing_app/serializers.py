from django.db.models import fields
from rest_framework import serializers
from mechdesing_app.models import Sensor, SensorData

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('ID','name')

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('ID','sensor','value')