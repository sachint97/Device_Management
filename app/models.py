from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=30,blank=False)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(blank=True)

    def __str__(self):
        return self.name