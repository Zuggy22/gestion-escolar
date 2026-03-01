from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('',       views.lista_cursos, name='lista'),
    path('crear/', views.crear_curso,  name='crear'),
]
