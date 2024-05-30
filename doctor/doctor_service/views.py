from django.shortcuts import render
from rest_framework.views import APIView
from .models import Doctor, WorkSchedule
from .serializers import DoctorSerializer, WorkScheduleSerializer, WorkScheduleCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
class DoctorListCreate(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetail(APIView):
    def get(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class WorkScheduleListCreate(APIView):
    def get(self, request):
        work_schedules = WorkSchedule.objects.all()
        serializer = WorkScheduleSerializer(work_schedules, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WorkScheduleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkScheduleDetail(APIView):
    def get(self, request, pk):
        work_schedule = get_object_or_404(WorkSchedule, pk=pk)
        serializer = WorkScheduleSerializer(work_schedule)
        return Response(serializer.data)
    
    def put(self, request, pk):
        work_schedule = get_object_or_404(WorkSchedule, pk=pk)
        serializer = WorkScheduleCreateSerializer(work_schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        work_schedule = get_object_or_404(WorkSchedule, pk=pk)
        work_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DoctorSearch(APIView):
    def get(self, request):
        specialty = request.query_params.get('specialty')
        name = request.query_params.get('name')
        if specialty:
            doctors = Doctor.objects.filter(specialty__icontains=specialty)
        elif name:
            doctors = Doctor.objects.filter(name__icontains=name)
        else:
            doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class DoctorWorkSchedule(APIView):
    def get(self, request, doctor_id):
        work_schedules = WorkSchedule.objects.filter(doctor_id=doctor_id)
        serializer = WorkScheduleSerializer(work_schedules, many=True)
        return Response(serializer.data)