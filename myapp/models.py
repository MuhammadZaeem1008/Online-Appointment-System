from django.db import models
from accounts.models import DoctorProfile,PatientProfile

class DoctorBio(models.Model):
    doctor=models.OneToOneField(DoctorProfile,on_delete=models.CASCADE,related_name='doctor_bio')
    about=models.TextField()
    education=models.TextField(max_length=200)
    experience=models.TextField(max_length=50)
    fees=models.IntegerField()
    def __str__(self):
        return self.doctor.user.get_full_name()

class DoctorTimeSlots(models.Model):
    doctor=models.OneToOneField(DoctorProfile,on_delete=models.CASCADE,related_name="doctor_time")
    is_available=models.BooleanField(default=False)
    time_slots=models.JSONField(default=list,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"time slots for {self.doctor.user.get_full_name()} ,last updated at {self.updated_at}"


