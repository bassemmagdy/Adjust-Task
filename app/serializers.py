from rest_framework.serializers import ModelSerializer
from .models import PerformanceMetric
from rest_framework import serializers


class PerformanceDataSerializer(ModelSerializer):
    cpi = serializers.FloatField(required=False, read_only=True)

    class Meta:
        model = PerformanceMetric
        fields = 'channel', 'country', 'impressions', 'clicks', 'date', 'spend', 'os', 'revenue', 'installs','cpi',