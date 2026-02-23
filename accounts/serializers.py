from rest_framework import serializers
from .models import User,DoctorProfile,PatientProfile

class DoctorSerializer(serializers.Serializer):
    license_no=serializers.CharField(write_only=True)
    specialization=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True,style={'input_type':'password'})
    class Meta:
        model=User
        fields=['first_name','last_name','email','password','license_no','specialization','mobile_number','city','gender']

