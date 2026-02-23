from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    ROLES=(
        ('doctor','Doctor'),
        ('patient','Patient')
    )
    GENDER=(
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    )
    role=models.CharField(max_length=20,choices=ROLES)
    mobile_number =models.CharField(max_length=15)
    city=models.CharField(max_length=20)
    gender=models.CharField(max_length=20,choices=GENDER)


class DoctorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctor_profile')
    specialization=models.CharField(max_length=200)
    license_number=models.CharField(max_length=12,unique=True)


    def __str__(self):
        return self.user.get_full_name()

class PatientProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient_profile')
    age=models.IntegerField(default=18)


