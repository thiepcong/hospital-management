from django.shortcuts import render
from .models import MedicalSupply, Medicine
from .serializers import MedicalSupplySerializer, MedicineSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class MedicineListCreate(APIView):
    def get(self, request):
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineDetail(APIView):
    def get(self, request, pk):
        try:
            medicine = Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            medicine = Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            medicine = Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicalSupplyListCreate(APIView):
    def get(self, request):
        medical_supplies = MedicalSupply.objects.all()
        serializer = MedicalSupplySerializer(medical_supplies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicalSupplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicalSupplyDetail(APIView):
    def get(self, request, pk):
        try:
            medical_supply = MedicalSupply.objects.get(pk=pk)
        except MedicalSupply.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicalSupplySerializer(medical_supply)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            medical_supply = MedicalSupply.objects.get(pk=pk)
        except MedicalSupply.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicalSupplySerializer(medical_supply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            medical_supply = MedicalSupply.objects.get(pk=pk)
        except MedicalSupply.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        medical_supply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)