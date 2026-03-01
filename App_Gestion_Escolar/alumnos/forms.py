"""
forms.py de la app Alumnos

PASO 4 DEL PDF (Parte III): Creando las Fichas de Inscripción.

Un formulario Django es una clase Python que describe:
  - Qué campos tiene el formulario
  - Qué tipo de dato acepta cada campo (texto, número, email, etc.)
  - Qué validaciones debe pasar cada campo

Django se encarga automáticamente de:
  - Generar el HTML del formulario
  - Validar los datos cuando llegan del usuario
  - Mostrar los errores si algo está mal
"""

from django import forms


class AlumnoForm(forms.Form):
    """
    Ficha de inscripción para un nuevo Alumno.
    Campos: nombre, apellido, edad, correo.
    """

    nombre = forms.CharField(
        max_length=100,
        label='Nombre',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: Valentina',
            'class': 'campo-form',
        })
    )

    apellido = forms.CharField(
        max_length=100,
        label='Apellido',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: Rojas Pérez',
            'class': 'campo-form',
        })
    )

    edad = forms.IntegerField(
        label='Edad',
        min_value=10,
        max_value=25,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ej: 15',
            'class': 'campo-form',
        })
    )

    correo = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Ej: alumno@liceo.cl',
            'class': 'campo-form',
        })
    )
