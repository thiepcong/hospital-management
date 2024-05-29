from rest_framework import serializers
from .models import Clinic, Bed

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name', 'location', 'total_beds', 'occupied_beds']

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['id', 'clinic', 'bed_number', 'is_occupied']