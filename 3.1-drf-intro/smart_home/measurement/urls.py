from django.urls import path

from measurement.views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-detail-update'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create')
]
