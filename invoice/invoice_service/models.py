from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_method = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment of {self.payment_method}"


class InvoiceDetail(models.Model):
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=50)
    unit = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.FloatField()
    note = models.CharField(max_length=100)
    invoice = models.ForeignKey('Invoice', related_name='details', on_delete=models.CASCADE)
    def __str__(self):
        return f"Invoice detail"
        
class Invoice(models.Model):
    patient_name = models.CharField(max_length=100)
    pharmacy_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    tax_code = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    status = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    cashier_id = models.IntegerField()
    deliver_id = models.IntegerField()
    def __str__(self):
        return f"Invoice for {self.patient_name}"


