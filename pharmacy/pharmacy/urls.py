from django.contrib import admin
from django.urls import path
from pharmacy_service.views import MedicalSupplyDetail, MedicalSupplyListCreate, MedicineDetail, MedicineListCreate, MedicineSearch, MedicalSupplySearch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/medicines/', MedicineListCreate.as_view(), name='medicine_list_create'),
    path('api/medicines/<int:pk>/', MedicineDetail.as_view(), name='medicine_detail'),
    path('api/medicines/search/', MedicineSearch.as_view(), name='medicine-search'),
    path('api/medical_supplies/', MedicalSupplyListCreate.as_view(), name='medical_supply_list_create'),
    path('api/medical_supplies/<int:pk>/', MedicalSupplyDetail.as_view(), name='medical_supply_detail'),
    path('api/medical_supplies/search/', MedicalSupplySearch.as_view(), name='medical-supply-search'),
]
