# https://www.youtube.com/watch?v=NoLF7Dlu5mc&t=1s
from rest_framework import serializers
from .models import Air_quality_metrics

class Air_quality_serializer(serializers.ModelSerializer):
   class Meta:
      model = Air_quality_metrics
      fields = '__all__'