from django.shortcuts import render
from rest_framework.views import APIView
from .models import Invoice, InvoiceDetail as Invoice_detail, Payment
from .serializers import InvoiceSerializer, PaymentSerializer, InvoiceDetailSerializer
from rest_framework.response import Response
from rest_framework import status
import requests

MEDICAL_SUPPLY_API = "http://127.0.0.1:8006/api/medical_supplies/"
MEDICINE_API = "http://127.0.0.1:8006/api/medicines/"
EMPLOYEE_ENDPOINT = "http://127.0.0.1:8004/api/employees/"
# Create your views here.

class PaymentAPIView(APIView):

    def get(self, request, format=None):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        payment = self.get_object(pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payment = self.get_object(pk)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        payment = self.get_object(pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InvoiceAPIView(APIView):
    def get(self, request, invoice_id):
        try:
            invoice = Invoice.objects.get(id=invoice_id)

            # Fetch and append payment details
            payment_serializer = PaymentSerializer(invoice.payment)

            # Fetch and append cashier details
            cashier_response = requests.get(EMPLOYEE_ENDPOINT + str(invoice.cashier_id))
            if cashier_response.status_code == 200:
                cashier_data = cashier_response.json()
                invoice.cashier_info = cashier_data

            # Fetch and append deliver details
            deliver_response = requests.get(EMPLOYEE_ENDPOINT + str(invoice.deliver_id))
            if deliver_response.status_code == 200:
                deliver_data = deliver_response.json()
                invoice.deliver_info = deliver_data

            # Fetch and append invoice details
            invoice_details = Invoice_detail.objects.filter(invoice=invoice)
            invoice_details_serializer = InvoiceDetailSerializer(invoice_details, many=True)

            # Create response data
            response_data = {
                "id": invoice.id,
                "patient_name": invoice.patient_name,
                "pharmacy_id": invoice.pharmacy_id,
                "tax_code": invoice.tax_code,
                "address": invoice.address,
                "phone_number": invoice.phone_number,
                "status": invoice.status,
                "payment": payment_serializer.data,
                "cashier_info": invoice.cashier_info,
                "deliver_info": invoice.deliver_info,
                "items": invoice_details_serializer.data
            }

            return Response(response_data)
        except Invoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['status'] = 1 

        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            invoice_data = serializer.validated_data
            res = {}    
            # Fetch and append cashier details
            cashier_response = requests.get(EMPLOYEE_ENDPOINT + str(request.data.get("cashier_id")))
            if cashier_response.status_code == 200:
                cashier_data = cashier_response.json()
                res['cashier_info'] = cashier_data

            # Fetch and append deliver details
            deliver_response = requests.get(EMPLOYEE_ENDPOINT + str(request.data.get("deliver_id")))
            if deliver_response.status_code == 200:
                deliver_data = deliver_response.json()
                res['deliver_info'] = deliver_data

            medical_supply_ids = invoice_data.pop('medical_supply_ids')
            medicine_ids = invoice_data.pop('medicine_ids')

            # Create the Invoice first
            invoice = Invoice.objects.create(
                patient_name=invoice_data['patient_name'],
                pharmacy_id=invoice_data['pharmacy_id'],
                tax_code=invoice_data['tax_code'],
                address=invoice_data['address'],
                phone_number=invoice_data['phone_number'],
                status=1,  # Set status to 1
                payment=invoice_data['payment'],
                cashier_id=invoice_data['cashier_id'],
                deliver_id=invoice_data['deliver_id']
            )

            all_items = []

            # Fetch and add medical supplies
            for supply in medical_supply_ids:
                product_id = supply.get('product_id')
                quantity = supply.get('quantity')
                supply_response = requests.get(f"{MEDICAL_SUPPLY_API}{product_id}")
                if supply_response.status_code == 200:
                    supply_data = supply_response.json()
                    supply_item = Invoice_detail.objects.create(
                        invoice=invoice,
                        product_name=supply_data['name'],
                        product_type='medical supply',
                        unit='Cái', 
                        quantity=quantity,
                        price=float(supply_data['price']),
                        note=supply_data.get('description', '')
                    )
                    supply_data['quantity'] = supply_data.get('quantity') - quantity
                    print(supply_data)
                    update_supply_quantity_res = requests.put(f"{MEDICAL_SUPPLY_API}{product_id}/", json = supply_data)
                    if update_supply_quantity_res.status_code != 200:
                        return Response({
                            "success" : False,
                            "message" : "medical supply quantity is invalid"
                        }, status=status.HTTP_400_BAD_REQUEST)
                    all_items.append(supply_item)

            # Fetch and add medicines
            for medicine in medicine_ids:
                product_id = medicine.get('product_id')
                quantity = medicine.get('quantity')
                medicine_response = requests.get(f"{MEDICINE_API}{product_id}")
                if medicine_response.status_code == 200:
                    medicine_data = medicine_response.json()
                    medicine_item = Invoice_detail.objects.create(
                        invoice=invoice,
                        product_name=medicine_data['name'],
                        product_type='medicine',
                        unit='Cái',
                        quantity=quantity,
                        price=float(medicine_data['price']),
                        note=medicine_data.get('description', '')
                    )
                    medicine_data['quantity'] = medicine_data.get('quantity') - quantity
                    update_medicine_quantity_res = requests.put(f"{MEDICINE_API}{product_id}/", json = medicine_data)
                    if update_medicine_quantity_res.status_code != 200:
                        return Response({
                            "success" : False,
                            "message" : "medicine quantity is invalid"
                        }, status=status.HTTP_400_BAD_REQUEST)
                    all_items.append(medicine_item)

            # Fetch and append invoice details
            invoice_details = Invoice_detail.objects.filter(invoice=invoice)
            invoice_details_serializer = InvoiceDetailSerializer(invoice_details, many=True)

            payment_serializer = PaymentSerializer(invoice.payment)
            res['payment'] = payment_serializer.data
            res['items'] = invoice_details_serializer.data
            invoice_serializer = InvoiceSerializer(invoice)
            res["id"] =  invoice_serializer.data.get("id")
            res["patient_name"] =  invoice_serializer.data.get("patient_name")
            res["pharmacy_id"] =  invoice_serializer.data.get("pharmacy_id")
            res["tax_code"] =  invoice_serializer.data.get("tax_code")
            res["address"] =  invoice_serializer.data.get("address")
            res["phone_number"] =  invoice_serializer.data.get("phone_number")
            res["status"] =  invoice_serializer.data.get("status")

            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)