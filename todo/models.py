from django.db import models
from app.models import MetaInfoBase


CHOICES = (
    ("high", "ALTA"),
    ("medium", "MEDIA"),
    ("low", "BAJA"),
)

# Create your models here.
class Task(MetaInfoBase):
    name = models.CharField(max_length=20, verbose_name="Nombre de la tarea")
    description = models.CharField(max_length=200, verbose_name="Descripcion de la tarea")
    priority = models.CharField(default="low", verbose_name="Prioridad de la tarea", max_length=10, choices=CHOICES)
    date_finish = models.DateTimeField(verbose_name="Fecha de finalizacion de la tarea")
    
    
    
    
    def save(self):
        self.name = self.name.upper()
        
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    