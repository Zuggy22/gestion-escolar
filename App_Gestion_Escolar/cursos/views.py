"""
views.py de la app Cursos — Parte III actualizado.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CursoForm


@login_required
def lista_cursos(request):
    cursos = [
        {'nombre': '1°A', 'nivel': 'Primero Medio',  'profesor_jefe': 'Prof. Ana Soto',      'alumnos': 35},
        {'nombre': '1°B', 'nivel': 'Primero Medio',  'profesor_jefe': 'Prof. Carlos Peña',   'alumnos': 33},
        {'nombre': '2°A', 'nivel': 'Segundo Medio',  'profesor_jefe': 'Prof. María Jiménez', 'alumnos': 31},
        {'nombre': '2°B', 'nivel': 'Segundo Medio',  'profesor_jefe': 'Prof. Roberto Lagos',  'alumnos': 34},
        {'nombre': '3°A', 'nivel': 'Tercero Medio',  'profesor_jefe': 'Prof. Claudia Vera',  'alumnos': 29},
    ]
    contexto = {'cursos': cursos, 'titulo': 'Lista de Cursos'}
    return render(request, 'cursos/lista_cursos.html', contexto)


@login_required
def crear_curso(request):
    if request.method == 'POST':
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            nombre_ramo = formulario.cleaned_data['nombre_ramo']
            jornada     = formulario.cleaned_data['jornada']
            nivel       = formulario.cleaned_data['nivel']
            contexto = {
                'nombre_ramo': nombre_ramo,
                'jornada':     jornada,
                'nivel':       nivel,
            }
            return render(request, 'cursos/resumen_curso.html', contexto)
    else:
        formulario = CursoForm()

    return render(request, 'cursos/crear_curso.html', {'formulario': formulario})
