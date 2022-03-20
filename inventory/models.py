from django.db import models

from app.models import MetaInfoBase

# Create your models here.
class Category(MetaInfoBase):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Category, self).save()

    class Meta:
        verbose_name_plural = "Categories"
