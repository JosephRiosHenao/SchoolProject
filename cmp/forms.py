from django import forms

from .models import *

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['description','location','contact','telphone','email']
        labels = {'description':'Descripcion', 'location':'Localizacion', 'contact':'Contacto','telphone':'Telefono','email':'Correo electronico'}
        
class BuyForm(forms.ModelForm):
    date_buy = forms.DateInput()
    date_fact = forms.DateInput()
    
    class Meta:
        model = BuyHead
        fields = ["provider","date_buy","observation","no_fact","date_fact","sub_total","offert","total"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['provider'].queryset = Provider.objects.all()
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields["date_buy"].widget.attrs["readonly"] = True
        self.fields["date_fact"].widget.attrs["readonly"] = True
        self.fields["sub_total"].widget.attrs["readonly"] = True
        self.fields["offert"].widget.attrs["readonly"] = True
        self.fields["total"].widget.attrs["readonly"] = True