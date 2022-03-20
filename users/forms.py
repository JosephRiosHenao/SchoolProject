from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='', max_length=100)
    name = forms.CharField(label='', max_length=100)
    last_name = forms.CharField(label='', max_length=100)
    password = forms.CharField(label='', widget=forms.PasswordInput())
    password_again = forms.CharField(label='', widget=forms.PasswordInput())
    email = forms.EmailField(label='')
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password_again = cleaned_data.get('password_again')
        if password != password_again:
            raise forms.ValidationError('Contraseñas no coinciden')
        return cleaned_data
    
    def user_duplicate(self):
        raise forms.ValidationError('Contraseñas no coinciden')