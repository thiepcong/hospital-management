from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name