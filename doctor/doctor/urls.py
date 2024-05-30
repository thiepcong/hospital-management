from django.contrib import admin
from django.urls import path
from doctor_service.views import DoctorDetail, DoctorListCreate, WorkScheduleDetail, WorkScheduleListCreate, DoctorSearch, DoctorWorkSchedule

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctors/', DoctorListCreate.as_view(), name='doctor_list_create'),
    path('api/doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor_detail'),
    path('api/work-schedules/', WorkScheduleListCreate.as_view(), name='work-schedule-list-create'),
    path('api/work-schedules/<int:pk>/', WorkScheduleDetail.as_view(), name='work-schedule-detail'),
    path('api/doctors/search/', DoctorSearch.as_view(), name='doctor-search'),
    path('api/doctors/<int:doctor_id>/work-schedules/', DoctorWorkSchedule.as_view(), name='doctor-work-schedules'),
]
