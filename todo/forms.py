from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    
    class Meta():
        model = Task
        fields = ('name', 'description', 'state', 'priority', 'date_finish')
        widgets = {
            'date_finish': forms.DateInput(attrs={'type': 'date'})
        }