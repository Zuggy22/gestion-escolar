"""
forms.py de la app Cursos

Ficha de inscripción para un nuevo Curso.
"""

from django import forms

JORNADAS = [
    ('',         '-- Seleccionar --'),
    ('Mañana',   'Mañana (08:00 - 14:00)'),
    ('Tarde',    'Tarde (14:00 - 20:00)'),
    ('Completa', 'Jornada Completa'),
]

NIVELES = [
    ('',               '-- Seleccionar --'),
    ('Primero Medio',  '1° Medio'),
    ('Segundo Medio',  '2° Medio'),
    ('Tercero Medio',  '3° Medio'),
    ('Cuarto Medio',   '4° Medio'),
]


class CursoForm(forms.Form):
    nombre_ramo = forms.CharField(
        max_length=100,
        label='Nombre del ramo / curso',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: Matemáticas 1°A',
            'class': 'campo-form',
        })
    )

    nivel = forms.ChoiceField(
        choices=NIVELES,
        label='Nivel',
        widget=forms.Select(attrs={'class': 'campo-form'})
    )

    jornada = forms.ChoiceField(
        choices=JORNADAS,
        label='Jornada',
        widget=forms.Select(attrs={'class': 'campo-form'})
    )
