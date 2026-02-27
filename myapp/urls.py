from django.urls import path
from .views import DoctorBioView,DoctorAvailability

urlpatterns=[
    path('doctor/bio/',DoctorBioView.as_view()),
    path('doctor/availability/',DoctorAvailability.as_view())
    # path('doctor/bio/<int:id>',DoctorBioView.as_view()),
]
