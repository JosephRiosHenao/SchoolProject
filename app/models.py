from django.db import models

from django.contrib.auth.models import User

class MetaInfoBase(models.Model):
    state = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_created")
    user_modified = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_modified", blank=True, null=True)
    
    class Meta:
        abstract = True
