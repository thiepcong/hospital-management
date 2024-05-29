from django.contrib import admin
from django.urls import path
from medical_record_service.views import MedicalRecordDetail, MedicalRecordListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/medical_records/', MedicalRecordListCreate.as_view(), name='medical_record_list_create'),
    path('api/medical_records/<int:pk>/', MedicalRecordDetail.as_view(), name='medical_record_detail'),
]
