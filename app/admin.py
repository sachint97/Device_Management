from django.contrib import admin
from app.models import Device
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_date', 'modified_date']


admin.site.register(Device, DeviceAdmin)