from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns=[
    path('doctor/register',DoctorRegister.as_view()),
    path('patient/register',PatientRegister.as_view()),
    path('login/',TokenObtainPairView.as_view())
]