from django.contrib import admin
from django.urls import path
from appointment_service.views import AppointmentDetail, AppointmentListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/appointments/', AppointmentListCreate.as_view(), name='appointment_list_create'),
    path('api/appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment_detail'),
]
