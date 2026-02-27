from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import DoctorRegisterSerializer,PatientRegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import authenticate
class PatientRegister(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializers=PatientRegisterSerializer(data=request.data)
        print(serializers)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

# Create your views here.

class DoctorRegister(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializers=DoctorRegisterSerializer(data=request.data)
        print("working")
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


