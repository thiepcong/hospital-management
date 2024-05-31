from django.shortcuts import render
from rest_framework.views import APIView
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class MedicalRecordListCreate(APIView):
    def get(self, request):
        medical_records = MedicalRecord.objects.all()
        serializer = MedicalRecordSerializer(medical_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        patient_id = request.data.get('patient_id')
        # Kiểm tra xem bệnh nhân có tồn tại trong Patient Service
        patient_service_url = f'http://127.0.0.1:8000/api/patients/{patient_id}/'
        patient_response = requests.get(patient_service_url)
        
        if patient_response.status_code != 200:
            return Response({"error": "Patient does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicalRecordDetail(APIView):
    def get(self, request, pk):
        try:
            medical_record = MedicalRecord.objects.get(pk=pk)
        except MedicalRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        patient_service_url = f'http://127.0.0.1:8000/api/patients/{medical_record.patient_id}/'
        patient_response = requests.get(patient_service_url)
        
        if patient_response.status_code != 200:
            return Response({"error": "Patient does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MedicalRecordSerializer(medical_record)
        data = serializer.data
        data['patient'] = patient_response.json()
        return Response(data)

    def put(self, request, pk):
        try:
            medical_record = MedicalRecord.objects.get(pk=pk)
        except MedicalRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicalRecordSerializer(medical_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            medical_record = MedicalRecord.objects.get(pk=pk)
        except MedicalRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        medical_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)