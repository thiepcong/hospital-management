from rest_framework import serializers
from .models import Medicine, MedicalSupply

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'description', 'quantity', 'price']

class MedicalSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalSupply
        fields = ['id', 'name', 'description', 'quantity', 'price']
