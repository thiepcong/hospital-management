from django.contrib import admin
from django.urls import path
from pharmacy_service.views import MedicalSupplyDetail, MedicalSupplyListCreate, MedicineDetail, MedicineListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicines/', MedicineListCreate.as_view(), name='medicine_list_create'),
    path('medicines/<int:pk>/', MedicineDetail.as_view(), name='medicine_detail'),
    path('medical_supplies/', MedicalSupplyListCreate.as_view(), name='medical_supply_list_create'),
    path('medical_supplies/<int:pk>/', MedicalSupplyDetail.as_view(), name='medical_supply_detail'),
]
