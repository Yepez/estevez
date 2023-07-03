from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Registro

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class RegistroForm(UserCreationForm):
    nombre_completo = forms.CharField(label='Nombre completo', max_length=255)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento')
    password1 = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', strip=False, widget=forms.PasswordInput)

    class Meta:
        model = Registro
        fields = ('nombre_completo', 'email', 'fecha_nacimiento', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if Registro.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Ya existe un registro con este correo electrónico.'))
        return email