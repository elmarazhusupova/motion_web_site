from rest_framework import serializers
from .models import ClubConsulting


class ClubConsultingSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClubConsulting
        fields = '__all__'
