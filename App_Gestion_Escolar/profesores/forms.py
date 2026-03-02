from django import forms
from .models import Profesor

ESPECIALIDADES = [
    ('', '-- Seleccionar --'),
    ('Matemáticas', 'Matemáticas'),
    ('Lenguaje',    'Lenguaje y Comunicación'),
    ('Ciencias',    'Ciencias Naturales'),
    ('Historia',    'Historia y Geografía'),
    ('Inglés',      'Inglés'),
    ('Educación Física', 'Educación Física'),
    ('Artes',       'Artes Visuales'),
    ('Otra',        'Otra'),
]


class ProfesorForm(forms.ModelForm):
    """
    ModelForm conectado al modelo Profesor.
    .save() guarda directamente en la base de datos.
    """
    class Meta:
        model  = Profesor
        fields = ['nombre', 'especialidad', 'años_experiencia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'campo-form',
                'placeholder': 'Ej: Ana Soto González'
            }),
            'especialidad': forms.Select(
                choices=ESPECIALIDADES,
                attrs={'class': 'campo-form'}
            ),
            'años_experiencia': forms.NumberInput(attrs={
                'class': 'campo-form',
                'placeholder': 'Ej: 8'
            }),
        }
        labels = {
            'nombre':           'Nombre completo',
            'especialidad':     'Especialidad / Asignatura',
            'años_experiencia': 'Años de experiencia',
        }