from django.contrib import admin
from django.urls import path
from clinic_bed_service.views import ClinicDetail, ClinicListCreate, BedDetail, BedListCreate,BedPatientListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clinics/', ClinicListCreate.as_view(), name='clinic_list_create'),
    path('api/clinics/<int:pk>/', ClinicDetail.as_view(), name='clinic_detail'),
    path('api/beds/', BedListCreate.as_view(), name='bed_list_create'),
    path('api/beds/<int:pk>/', BedDetail.as_view(), name='bed_detail'),
    path('api/bedPatient/', BedPatientListCreate.as_view(), name='bed_detail'),
    path('api/bedPatient/<int:pk>/', BedPatientListCreate.as_view(), name='bed_detail'),
]
