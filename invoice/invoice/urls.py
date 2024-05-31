from django.contrib import admin
from django.urls import path, include
from invoice_service.views import InvoiceAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/invoice/', InvoiceAPIView.as_view()),
    path('api/invoice/<int:invoice_id>', InvoiceAPIView.as_view()),
]
