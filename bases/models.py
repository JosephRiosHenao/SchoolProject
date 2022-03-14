from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ClassModel(models.Model):
    state = models.BooleanField(default=True),
    create_date = models.DateTimeField(auto_now_add=True),
    modified_date = models.DateTimeField(auto_now=True),
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    user_modified = models.ForeignKey(User, on_delete=models.CASCADE)