from rest_framework.serializers import ModelSerializer
from .models import DoctorBio,DoctorTimeSlots


class DoctorBioSerializer(ModelSerializer):
    class Meta:
        model=DoctorBio
        fields=['id','about','education','experience','fees']

class DoctorTimeSlotsSerializer(ModelSerializer):
    class Meta:
        model=DoctorTimeSlots
        fields=["time_slots","is_available","updated_at"]
