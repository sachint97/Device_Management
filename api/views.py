from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from app.models import Device
from rest_framework.response import Response
from api.serializer import DeviceSerializer
# Create your views here.

class DeviceUpdateView(APIView):
    def put(self,request,pk):
        try:
            device = Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            return Response({"error": "Device not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DeviceSerializer(device ,data = request.data)
        serializer.is_valid(raise_exception=True)
        device.modified_date = serializer.validated_data.get('modified_date', device.modified_date)
        device.save()
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
