from email.headerregistry import Address
from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.Patient.name


class Staff(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Prescription(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    advice = models.TextField()

    def __str__(self):
        return self.Patient.name
