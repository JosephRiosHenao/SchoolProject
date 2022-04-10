from django.db import models

from app.models import MetaInfoBase

# Create your models here.
class Category(MetaInfoBase):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    def save(self):
        self.description = self.description.upper()
        super(Category, self).save()

    class Meta:
        verbose_name_plural = "Categories"
