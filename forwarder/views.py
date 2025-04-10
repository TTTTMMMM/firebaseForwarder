# https://www.youtube.com/watch?v=NoLF7Dlu5mc&t=1s
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Air_quality_metrics
from .serializer import Air_quality_serializer
    
@api_view(['GET'])
def get_air_quality_metric(request):
   last_measurement = Air_quality_metrics.objects.latest('id')
   serialized = Air_quality_serializer(last_measurement)
   return Response(serialized.data)

@api_view(['POST'])
def create_air_quality_metric(request):
   serializer = Air_quality_serializer(data=request.data)
   if(serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)