from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Asset(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    model_number = models.CharField(max_length=250)
    serial_number = models.CharField(max_length=250)
    registration_date = models.DateField(null=True)
    warranty = models.BooleanField(null=True, blank=True)
    warranty_expiry = models.DateField(null=True, blank=True)
    personal_device = models.BooleanField(null=True)
    location = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(null=True)