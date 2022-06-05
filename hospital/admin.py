from django.contrib import admin

from hospital.models import Appointment, Doctor, Patient, Prescription, Staff

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Staff)
admin.site.register(Prescription)
