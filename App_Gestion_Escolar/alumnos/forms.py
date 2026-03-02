from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    """
    ModelForm: conectado al modelo Alumno.
    .save() guarda directamente en la base de datos.
    """
    class Meta:
        model  = Alumno
        fields = ['nombre', 'apellido', 'edad', 'correo', 'curso', 'promedio']
        widgets = {
            'nombre':   forms.TextInput(attrs={'class': 'campo-form', 'placeholder': 'Ej: Valentina'}),
            'apellido': forms.TextInput(attrs={'class': 'campo-form', 'placeholder': 'Ej: Rojas'}),
            'edad':     forms.NumberInput(attrs={'class': 'campo-form', 'placeholder': 'Ej: 15'}),
            'correo':   forms.EmailInput(attrs={'class': 'campo-form', 'placeholder': 'Ej: alumno@liceo.cl'}),
            'curso':    forms.TextInput(attrs={'class': 'campo-form', 'placeholder': 'Ej: 1°A'}),
            'promedio': forms.NumberInput(attrs={'class': 'campo-form', 'placeholder': 'Ej: 5.8'}),
        }