from django.db import models
from django.contrib.auth.models import User

# References
# Django (no date) Model field reference | Django documentation | Django. Available at: https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey (accessed 10 October 2022).
# Django (no date) Models | Django documentation | Django. Available at: https://docs.djangoproject.com/en/4.1/topics/db/models/#module-django.db.models (accessed 10 October 2022b).
# Django (no date) Writing your first Django app, part 2 | Django documentation | Django. Available at: https://docs.djangoproject.com/en/4.1/intro/tutorial02/ (accessed 10 October 2022c).
# SQLite (no date) Datatypes In SQLite. Available at: https://www.sqlite.org/datatype3.html (accessed 10 October 2022).


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