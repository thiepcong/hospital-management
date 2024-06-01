from django.contrib import admin

from .models import Clinic, Bed, BedPatient

# Register your models here.
admin.site.register(Clinic)
admin.site.register(Bed)
admin.site.register(BedPatient)