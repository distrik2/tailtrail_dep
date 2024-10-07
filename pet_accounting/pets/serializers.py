from rest_framework import serializers
from .models import PetProfile

class PetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetProfile
        fields = '__all__'
