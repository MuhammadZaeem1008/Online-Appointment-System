from django.shortcuts import render
from rest_framework.response import Response
from .serializers import DoctorBioSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from accounts.models import DoctorProfile,User
from .models import DoctorBio,DoctorTimeSlots
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsDoctor
from .serializers import DoctorTimeSlotsSerializer
class DoctorBioView(APIView):
    permission_classes = [IsAuthenticated,IsDoctor]
    def post(self,request):
        user=request.user
        doctor_profile=DoctorProfile.objects.get(user=user)
        serializer=DoctorBioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(doctor=doctor_profile)
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self,request):
        id=request.GET.get('id')
        data=DoctorBio.objects.get(id=id)
        serializer=DoctorBioSerializer(data)
        return Response(serializer.data)

class DoctorAvailability(APIView):
    permission_classes = [IsAuthenticated,IsDoctor]
    def post(self,request):
        user=request.user.doctor_profile
        serializer=DoctorTimeSlotsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(doctor=user)
            return Response(f"Doctor {request.user.first_name} Slots are set ")
    def patch(self,request):
        is_available=request.GET.get("is_available")
        doctor_user=request.user.doctor_profile
        try:
            DoctorTimeSlots.objects.filter(doctor=doctor_user).update(is_available=is_available)
            return Response(f"Availability for the doctor {request.user.get_full_name()} is marked as {is_available}")
        except:
            return Response("Unable to update ")





