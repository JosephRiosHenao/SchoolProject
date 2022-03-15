from django.db import models

from bases.models import ModelBase

# Create your models here.
class Category(ModelBase):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Category, self).save()

    class Meta:
        verbose_name_plural = "Categories"
