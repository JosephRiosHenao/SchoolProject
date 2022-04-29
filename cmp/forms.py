from django import forms

from .models import *

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['description','location','contact','telphone','email']
        labels = {'description':'Descripcion', 'location':'Localizacion', 'contact':'Contacto','telphone':'Telefono','email':'Correo electronico'}