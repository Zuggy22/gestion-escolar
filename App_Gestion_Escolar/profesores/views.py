"""
views.py de la app Profesores — Parte III actualizado.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfesorForm


@login_required
def lista_profesores(request):
    profesores = [
        {'nombre': 'Prof. Ana Soto',      'asignatura': 'Matemáticas', 'años_exp': 12},
        {'nombre': 'Prof. Carlos Peña',   'asignatura': 'Lenguaje',    'años_exp': 8},
        {'nombre': 'Prof. María Jiménez', 'asignatura': 'Ciencias',    'años_exp': 15},
        {'nombre': 'Prof. Roberto Lagos', 'asignatura': 'Historia',    'años_exp': 6},
        {'nombre': 'Prof. Claudia Vera',  'asignatura': 'Inglés',      'años_exp': 10},
    ]
    contexto = {'profesores': profesores, 'titulo': 'Lista de Profesores'}
    return render(request, 'profesores/lista_profesores.html', contexto)


@login_required
def crear_profesor(request):
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            nombre       = formulario.cleaned_data['nombre']
            especialidad = formulario.cleaned_data['especialidad']
            años_exp     = formulario.cleaned_data['años_experiencia']
            contexto = {
                'nombre':       nombre,
                'especialidad': especialidad,
                'años_exp':     años_exp,
            }
            return render(request, 'profesores/resumen_profesor.html', contexto)
    else:
        formulario = ProfesorForm()

    return render(request, 'profesores/crear_profesor.html', {'formulario': formulario})
