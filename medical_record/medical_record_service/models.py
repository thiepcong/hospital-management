from django.db import models

# Create your models here.

class MedicalRecord(models.Model):
    patient_id = models.IntegerField()  # Chỉ lưu trữ ID bệnh nhân từ Patient Service
    diagnosis = models.TextField()
    treatment = models.TextField()
    test_results = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Medical Record for Patient ID {self.patient_id} on {self.date}"