"""
views.py de la app Alumnos — Parte III actualizado.

PASO 3 DEL PDF (Parte III): Blindando las Aulas.
Importamos login_required y lo colocamos como "guardia"
encima de cada vista privada con @login_required.

Si alguien intenta entrar a /alumnos/ sin sesión iniciada,
Django lo redirige automáticamente al LOGIN_URL ('login').

PASO 5 DEL PDF (Parte III): Procesando el POST.
La vista crear_alumno maneja dos situaciones:
  - GET  → muestra el formulario vacío
  - POST → valida los datos y muestra el resumen
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # El guardia de seguridad
from .forms import AlumnoForm


# El decorador @login_required es el "guardia en la puerta".
# Si no tienes sesión activa, te manda al login antes de dejarte pasar.
@login_required
def lista_alumnos(request):
    alumnos = [
        {'nombre': 'Valentina Rojas',   'curso': '1°A', 'promedio': 6.2},
        {'nombre': 'Matías González',   'curso': '1°B', 'promedio': 5.8},
        {'nombre': 'Camila Fuentes',    'curso': '2°A', 'promedio': 6.7},
        {'nombre': 'Sebastián Morales', 'curso': '2°B', 'promedio': 4.9},
        {'nombre': 'Isidora Vargas',    'curso': '3°A', 'promedio': 6.4},
        {'nombre': 'Nicolás Castro',    'curso': '3°B', 'promedio': 5.5},
    ]
    contexto = {'alumnos': alumnos, 'titulo': 'Lista de Alumnos'}
    return render(request, 'alumnos/lista_alumnos.html', contexto)


@login_required
def crear_alumno(request):
    """
    Vista para crear un nuevo alumno.

    PASO 5 DEL PDF (Parte III):
    La vista pregunta: ¿el método de la solicitud es GET o POST?

    GET  → El usuario llegó a la página por primera vez.
           Mostramos el formulario vacío.

    POST → El usuario llenó el formulario y lo envió.
           Validamos los datos con is_valid().
           Si son válidos, extraemos con cleaned_data y mostramos resumen.
           Si no son válidos, volvemos a mostrar el formulario con los errores.
    """

    if request.method == 'POST':
        # El usuario envió el formulario → le pasamos los datos que llegaron
        formulario = AlumnoForm(request.POST)

        if formulario.is_valid():
            # cleaned_data contiene los datos ya validados y limpios
            nombre   = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            edad     = formulario.cleaned_data['edad']
            correo   = formulario.cleaned_data['correo']

            # Enviamos los datos al template de confirmación
            contexto = {
                'nombre':   nombre,
                'apellido': apellido,
                'edad':     edad,
                'correo':   correo,
            }
            return render(request, 'alumnos/resumen_alumno.html', contexto)

        # Si el formulario NO es válido, lo devolvemos con los errores marcados
    else:
        # Es un GET → creamos un formulario completamente vacío
        formulario = AlumnoForm()

    return render(request, 'alumnos/crear_alumno.html', {'formulario': formulario})
