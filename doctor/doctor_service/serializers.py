from rest_framework import serializers
from .models import Doctor, WorkSchedule

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class WorkScheduleCreateSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = WorkSchedule
        fields = '__all__'

class WorkScheduleSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = WorkSchedule
        fields = '__all__'
