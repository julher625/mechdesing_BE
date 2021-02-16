from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sensor$',views.SensorList.as_view()),
    url(r'sensor/(?P<pk>[0-9]+)$',views.SensorDetail.as_view()),
    url(r'^sensordata$',views.SensorDataList.as_view()),
    url(r'sensordata/(?P<pk>[0-9]+)$',views.SensorDataDetail.as_view())
]