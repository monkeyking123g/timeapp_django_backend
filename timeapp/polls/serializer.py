from rest_framework import serializers
from .models import *

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'

class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Totale
        fields = '__all__'