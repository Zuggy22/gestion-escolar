"""
forms.py de la app Profesores

Ficha de inscripción para un nuevo Profesor.
"""

from django import forms

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


class ProfesorForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label='Nombre completo',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: Ana Soto González',
            'class': 'campo-form',
        })
    )

    especialidad = forms.ChoiceField(
        choices=ESPECIALIDADES,
        label='Especialidad / Asignatura',
        widget=forms.Select(attrs={'class': 'campo-form'})
    )

    años_experiencia = forms.IntegerField(
        label='Años de experiencia',
        min_value=0,
        max_value=50,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ej: 8',
            'class': 'campo-form',
        })
    )
