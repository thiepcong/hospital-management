from invoice_service.views import InvoiceListCreate, InvoiceDetail, PaymentListCreate, PaymentDetail
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/invoices/', InvoiceListCreate.as_view(), name='invoice_list_create'),
    path('api/invoices/<int:pk>/', InvoiceDetail.as_view(), name='invoice_detail'),
    path('api/payments/', PaymentListCreate.as_view(), name='payment_list_create'),
    path('api/payments/<int:pk>/', PaymentDetail.as_view(), name='payment_detail'),
]
