from django.db import models

class Sensor(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    name = models.TextField()

class SensorData(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    sensor = models.ForeignKey(Sensor,null=True,on_delete=models.SET_NULL)
    value = models.FloatField()
    