from rest_framework import serializers
from .models import User,DoctorProfile,PatientProfile

class   DoctorRegisterSerializer(serializers.ModelSerializer):
    license_number=serializers.CharField(write_only=True)
    specialization=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True,style={'input_type':'password'})
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','license_number','specialization','mobile_number','city','gender']

    def validate_email(self,value):
        if value=="":
            raise serializers.ValidationError("Email is required")
        return value
    def create(self, validated_data):
        license_number=validated_data.pop('license_number')
        specialization=validated_data.pop('specialization')
        password=validated_data.pop('password')
        user=User.objects.create(role='doctor',**validated_data)
        user.set_password(password)
        user.save()
        DoctorProfile.objects.create(user=user,license_number=license_number,specialization=specialization)
        return user



class PatientRegisterSerializer(serializers.ModelSerializer):
    age=serializers.IntegerField(write_only=True)
    password=serializers.CharField(write_only=True,style={'input_type':'password'})
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','age','mobile_number','city','gender']
    def create(self,validated_data):
        age=validated_data.pop('age')
        password=validated_data.pop('password')
        user=User.objects.create(role='patient',**validated_data)
        user.set_password(password)
        user.save()
        PatientProfile.objects.create(user=user,age=age)
        return

