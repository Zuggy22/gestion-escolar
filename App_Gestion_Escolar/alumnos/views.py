from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Alumno
from .forms import AlumnoForm


@login_required
def lista_alumnos(request):
    busqueda = request.GET.get('q', '')
    if busqueda:
        alumnos = Alumno.objects.filter(
            nombre__icontains=busqueda
        ) | Alumno.objects.filter(
            apellido__icontains=busqueda
        )
    else:
        alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista_alumnos.html', {
        'alumnos':  alumnos,
        'titulo':   'Lista de Alumnos',
        'busqueda': busqueda,
    })


@login_required
def crear_alumno(request):
    if request.method == 'POST':
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            alumno = formulario.save()
            messages.success(request, f'✅ El alumno {alumno.nombre} {alumno.apellido} fue matriculado exitosamente.')
            return redirect('alumnos:lista')
    else:
        formulario = AlumnoForm()
    return render(request, 'alumnos/crear_alumno.html', {'formulario': formulario})


@login_required
def editar_alumno(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = AlumnoForm(request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'✅ Los datos de {alumno.nombre} {alumno.apellido} fueron actualizados.')
            return redirect('alumnos:lista')
    else:
        formulario = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/crear_alumno.html', {'formulario': formulario})


@login_required
def eliminar_alumno(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    if request.method == 'POST':
        nombre = f'{alumno.nombre} {alumno.apellido}'
        alumno.delete()
        messages.error(request, f'🗑️ El alumno {nombre} fue eliminado del sistema.')
        return redirect('alumnos:lista')
    return render(request, 'alumnos/confirmar_eliminar.html', {'objeto': alumno})