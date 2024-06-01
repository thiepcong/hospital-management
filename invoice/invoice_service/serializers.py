from rest_framework import serializers
from .models import Invoice, Payment, InvoiceDetail

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceDetailSerializer(many=True, read_only=True)
    medical_supply_ids = serializers.ListField(write_only=True)
    medicine_ids = serializers.ListField(write_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'patient_name', 'pharmacy_id', 'tax_code', 'address', 'phone_number', 'cashier_id', 'deliver_id', 'status', 'payment', 'items', 'medical_supply_ids', 'medicine_ids']
