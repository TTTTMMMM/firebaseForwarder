# https://www.youtube.com/watch?v=NoLF7Dlu5mc&t=1s
from django.urls import path
from .views import get_air_quality_metric
from .views import create_air_quality_metric

urlpatterns = [
    path('metrics/', get_air_quality_metric, name='get_air_quality_metric'),
    path('metrics/create/', create_air_quality_metric, name='create_air_quality_metric')
]
