from django.contrib import admin
from .models import MedicalSupply, Medicine
# Register your models here.

admin.site.register(MedicalSupply)
admin.site.register(Medicine)