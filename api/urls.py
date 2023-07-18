from django.urls import path
from api.views import DeviceUpdateView

urlpatterns = [
    path("device-update/<int:pk>",DeviceUpdateView.as_view(),name="device_update")
]