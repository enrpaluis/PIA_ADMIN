from django import forms
from .models import Equipo
from .models import Mantenimiento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EquipoForm(forms.ModelForm):
    class Meta:
        model=Equipo
        fields='__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class ManteForm(forms.ModelForm):
    class Meta:
        model=Mantenimiento
        fields='__all__'