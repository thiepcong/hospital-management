from django.contrib import admin
from django.urls import path
from employee_service.views import EmployeeDetail, EmployeeListCreate, EmployeeSearch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', EmployeeListCreate.as_view(), name='employee_list_create'),
    path('api/employees/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('api/employees/search/', EmployeeSearch.as_view(), name='employee-search'),
]
