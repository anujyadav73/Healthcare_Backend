from django.contrib.auth.models import User
from django.db import models

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# class PatientDoctorMapping(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctor_mappings")
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patient_mappings")
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.patient.name} - {self.doctor.name}"