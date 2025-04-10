# https://www.youtube.com/watch?v=NoLF7Dlu5mc&t=1s
from django.db import models
from django.utils import timezone
from datetime import datetime


def current_datetime():
    return datetime.now(timezone())

class Air_quality_metrics(models.Model):
   dt = models.DateTimeField(default=timezone.now)
   temperature = models.FloatField()
   humidity = models.FloatField()
   eCO2 = models.IntegerField()
   TVOC = models.IntegerField()

   def __str__(self):
      return(f"{self.time} \n   {self.temperature} F, {self.humdity}%, {self.eCO2} ppm, {self.TVOC} ppb")