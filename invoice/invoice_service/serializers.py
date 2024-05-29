from rest_framework import serializers
from .models import Invoice, Payment

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'patient_name', 'total_amount', 'created_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'invoice', 'amount_paid', 'payment_method', 'payment_date']
