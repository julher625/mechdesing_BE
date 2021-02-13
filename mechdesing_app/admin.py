from django.contrib import admin

from mechdesing_app.models import Sensor, SensorData


admin.site.register(Sensor)
admin.site.register(SensorData)