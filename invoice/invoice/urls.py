from django.contrib import admin
from django.urls import path, include
from invoice_service.views import InvoiceAPIView, PaymentAPIView, PaymentDetailAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/invoice/', InvoiceAPIView.as_view()),
    path('api/invoice/<int:invoice_id>', InvoiceAPIView.as_view()),
    path('api/payments/', PaymentAPIView.as_view(), name='payment-list'),
    path('api/payments/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
]
