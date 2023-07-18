from django import forms
from app.models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
        }
