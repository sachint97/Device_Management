from django.urls import path
from app.views import device_list,create_device

urlpatterns = [
    path("home/",device_list,name="device_list"),
    path("create/",create_device,name="create_device")
]
