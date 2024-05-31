from rest_framework import serializers
from .models import Clinic, Bed, BedPatient

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = "__all__"
class BedPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedPatient
        fields = "__all__"