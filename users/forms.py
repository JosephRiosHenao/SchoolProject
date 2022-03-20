from django import forms

from django.contrib.auth.models import User 

from users.models import Profile

class RegisterForm(forms.Form):
    username = forms.CharField(label='', max_length=100)
    first_name = forms.CharField(label='', max_length=100)
    last_name = forms.CharField(label='', max_length=100)
    password = forms.CharField(label='', widget=forms.PasswordInput())
    password_again = forms.CharField(label='', widget=forms.PasswordInput())
    email = forms.EmailField(label='')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya existe')
        return username
    
    def clean(self):
        data = super().clean()
        password = data['password']
        password_again = data['password_again']
        if password != password_again:
            raise forms.ValidationError('Contraseñas no coinciden')
        return data
    
    def save(self):
        data = self.cleaned_data
        data.pop('password_again')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()