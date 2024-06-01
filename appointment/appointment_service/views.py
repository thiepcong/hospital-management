from django.shortcuts import render
from rest_framework.views import APIView
from .models import Appointment
from .serializers import AppointmentSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
import datetime

# Create your views here.


class AppointmentListCreate(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request):
        patient_id = request.data.get('patient_id')
        patient_service_url = f'http://127.0.0.1:8000/api/patients/{patient_id}/'
        patient_response = requests.get(patient_service_url)

        if patient_response.status_code != 200:
            return Response({"error": "Patient does not exist"}, status=status.HTTP_404_NOT_FOUND)

        doctor_id = request.data.get('doctor_id')
        doctor_service_url = f'http://127.0.0.1:8003/api/doctors/{doctor_id}/'
        doctor_response = requests.get(doctor_service_url)
        if doctor_response.status_code != 200:
            return Response({"error": "Doctor  does not exist"}, status=status.HTTP_404_NOT_FOUND)

        work_schedules_url = f'http://127.0.0.1:8003/api/doctors/{doctor_id}/work-schedules/'
        work_schedules_response = requests.get(work_schedules_url)
        if work_schedules_response.status_code != 200:
            return Response({"error": "Could not retrieve doctor's work schedules"}, status=status.HTTP_400_BAD_REQUEST)

        work_schedules = work_schedules_response.json()

        appointment_date_str = request.data.get('date')
        appointment_time_str = request.data.get('time')
        appointment_datetime_str = f"{appointment_date_str} {appointment_time_str}"
        appointment_datetime = datetime.datetime.strptime(appointment_datetime_str, '%Y-%m-%d %H:%M:%S')
        appointment_day_of_week = appointment_datetime.strftime('%A')

        valid_appointment = False
        for schedule in work_schedules:
            if schedule['day_of_week'] == appointment_day_of_week:
                start_time = datetime.datetime.strptime(schedule['start_time'], '%H:%M:%S').time()
                end_time = datetime.datetime.strptime(schedule['end_time'], '%H:%M:%S').time()
                appointment_time_obj = appointment_datetime.time()

                if start_time <= appointment_time_obj <= end_time:
                    valid_appointment = True
                    break

        if not valid_appointment:
            return Response({"error": "Appointment time is outside the doctor's work schedule"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetail(APIView):
    def get(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
