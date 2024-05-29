from django.db import models

class Appointment(models.Model):
    patient_id = models.IntegerField()  
    doctor_id = models.IntegerField()  
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Appointment for Patient ID {self.patient_id} on {self.date} at {self.time}"
