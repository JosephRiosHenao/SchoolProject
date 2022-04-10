from django import forms

from .models import *

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
    
    class Meta():
        model = Category
        fields = ['description','state']
        labels = {'description':"Descripcion",'state':"Estado"}
        widget = {'description': forms.TextInput} 
        

class SubCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubCategoryForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class':'form-control w-100 m-2'})
    
    class Meta():
        model = SubCategory
        fields = ['description','category','state']
        labels = {'description':"Descripcion",'category':"Categoria",'state':"Estado"}
        widget = {'description': forms.TextInput, 'category': forms.ModelChoiceField(queryset=Category.objects.all())}