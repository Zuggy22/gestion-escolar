from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from alumnos.models import Alumno
from profesores.models import Profesor
from cursos.models import Curso


@login_required
def inicio(request):
    contexto = {
        'total_alumnos':    Alumno.objects.count(),
        'total_profesores': Profesor.objects.count(),
        'total_cursos':     Curso.objects.count(),
        'alumnos_riesgo':   Alumno.objects.filter(promedio__lt=5.5).count(),
    }
    return render(request, 'inicio.html', contexto)