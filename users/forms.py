from django import forms

from django.contrib.auth.models import User 

from colorfield.widgets import ColorWidget

from users.models import Profile

class RegisterForm(forms.Form):
    username = forms.CharField(label='', max_length=100)
    first_name = forms.CharField(label='', max_length=100)
    last_name = forms.CharField(label='', max_length=100)
    password = forms.CharField(label='', widget=forms.PasswordInput())
    password_again = forms.CharField(label='', widget=forms.PasswordInput())
    email = forms.EmailField(label='')
    
    class Meta:
        model = Profile
        fields = ['username','first_name','last_name','password','password_again','email']
    
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
        return profile
        
# class ProfileForm(forms.Form):
#     color_primary = forms.CharField(label='Color primario', max_length=7,
#         widget=forms.TextInput(attrs={'type': 'color'}))
#     color_secondary = forms.CharField(label='Color secundario', max_length=7,
#         widget=forms.TextInput(attrs={'type': 'color'}))
    
#     class Meta:
#         model = Profile
#         fields = ['website', 'twitter', 'instagram', 'facebook', 'bio', 'phone', 'organization', 'location', 'gender', 'picture', 'color_primary', 'color_secondary']
    