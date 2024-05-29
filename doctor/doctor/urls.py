from django.contrib import admin
from django.urls import path
from doctor_service.views import DoctorDetail, DoctorListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctors/', DoctorListCreate.as_view(), name='doctor_list_create'),
    path('api/doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor_detail'),
]
