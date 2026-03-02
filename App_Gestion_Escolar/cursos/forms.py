from django import forms
from .models import Curso
from profesores.models import Profesor


class CursoForm(forms.ModelForm):
    """
    ModelForm conectado al modelo Curso.
    El campo profesor_jefe carga los profesores desde la base de datos.
    """
    class Meta:
        model  = Curso
        fields = ['nombre_ramo', 'nivel', 'jornada', 'profesor_jefe']
        widgets = {
            'nombre_ramo':   forms.TextInput(attrs={
                'class': 'campo-form',
                'placeholder': 'Ej: Matemáticas 1°A'
            }),
            'nivel':         forms.Select(attrs={'class': 'campo-form'}),
            'jornada':       forms.Select(attrs={'class': 'campo-form'}),
            'profesor_jefe': forms.Select(attrs={'class': 'campo-form'}),
        }
        labels = {
            'nombre_ramo':   'Nombre del ramo',
            'nivel':         'Nivel',
            'jornada':       'Jornada',
            'profesor_jefe': 'Profesor Jefe',
        }