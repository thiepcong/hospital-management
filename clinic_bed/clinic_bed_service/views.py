from django.shortcuts import render
import requests
from .models import Clinic, Bed, BedPatient
from rest_framework.views import APIView
from .serializers import ClinicSerializer, BedSerializer,BedPatientSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class ClinicListCreate(APIView):
    def get(self, request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClinicDetail(APIView):
    def get(self, request, pk):
        try:
            clinic = Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClinicSerializer(clinic)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            clinic = Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClinicSerializer(clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            clinic = Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        clinic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BedListCreate(APIView):
    def get(self, request):
        beds = Bed.objects.all()
        serializer = BedSerializer(beds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BedDetail(APIView):
    def get(self, request, pk):
        try:
            bed = Bed.objects.get(pk=pk)
        except Bed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BedSerializer(bed)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            bed = Bed.objects.get(pk=pk)
        except Bed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BedSerializer(bed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            bed = Bed.objects.get(pk=pk)
        except Bed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        bed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# thêm bệnh nhân vào giường bệnh sử dụng post
class BedPatientListCreate(APIView):
    def post(self, request):
        serializer = BedPatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, pk):
        try:
            bed = BedPatient.objects.filter(pk=pk).order_by('-date_occupied').first()
        except BedPatient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if(bed == None):
            return Response(status=status.HTTP_404_NOT_FOUND)
        patient_service_url = f'http://127.0.0.1:8000/api/patients/{bed.patient_id}/'
        patient_response = requests.get(patient_service_url)
        
        if patient_response.status_code != 200:
            return Response({"error": "Patient does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BedPatientSerializer(bed)
        data = serializer.data
        print(patient_response.json())
        data['patient'] = patient_response.json()
        return Response(data)