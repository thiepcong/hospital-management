from django.contrib import admin
from django.urls import path
from patient_service.views import PatientDetail, PatientListCreate, PatientSearch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/patients/', PatientListCreate.as_view(), name='patient_list_create'),
    path('api/patients/<int:pk>/', PatientDetail.as_view(), name='patient_detail'),
    path('api/patients/search/', PatientSearch.as_view(), name='patient-search'),
]
