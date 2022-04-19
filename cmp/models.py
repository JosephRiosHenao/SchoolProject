from django.db import models

from app.models import MetaInfoBase

# Create your models here.
class Provider(MetaInfoBase):
    description = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    contact = models.CharField(max_length=100)
    telphone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
