from django.contrib import admin
from .models import Payment, Invoice, InvoiceDetail

admin.site.register(Payment)
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
# Register your models here.
