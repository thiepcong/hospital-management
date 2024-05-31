from django.db import models

# Create your models here.
class Clinic(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_beds = models.IntegerField(default=0)
    occupied_beds = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Bed(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    bed_number = models.IntegerField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.bed_number} at {self.clinic.name}"

class BedPatient(models.Model):
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    patient_id = models.IntegerField()
    date_occupied = models.DateField()
    date_vacated = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Bed {self.bed.bed_number} at {self.bed.clinic.name} occupied by Patient ID {self.patient_id}"