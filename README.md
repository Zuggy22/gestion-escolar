# Gestion Escolar

📖 Descripción General
El Sistema de Gestión Escolar del Liceo Municipal es una aplicación web desarrollada como proyecto de bootcamp en Python y Django. Su propósito es digitalizar y centralizar los procesos administrativos y académicos de un establecimiento educacional, reemplazando el uso de planillas y documentos físicos por una plataforma moderna, segura y fácil de usar.
El sistema fue construido de forma incremental, cubriendo desde el CRUD básico hasta funcionalidades avanzadas como predicciones con inteligencia artificial, generación de informes PDF y un canal de comunicación entre apoderados y profesores.

✨#Funcionalidades

👩‍🎓 Gestión de Alumnos

Registro completo con nombre, apellido, edad, correo y curso
Búsqueda en tiempo real por nombre o apellido
Edición y eliminación con confirmación
Vista de resumen post-matrícula con accesos rápidos

👨‍🏫 Gestión de Profesores

Registro de planta docente con especialidad y años de experiencia
Badge automático de categoría Senior (≥ 10 años de experiencia)
Buscador por nombre y especialidad

📚 Gestión de Cursos

Creación de cursos con nivel, jornada y asignación de profesor jefe
Relación directa con alumnos y profesores del sistema

📊 Sistema de Notas

Registro de hasta 4 evaluaciones por asignatura por alumno
7 asignaturas disponibles: Lenguaje, Matemáticas, Ciencias, Historia, Inglés, Educación Física y Artes
Cálculo automático de promedio por asignatura y promedio final
Actualización automática del promedio del alumno en base de datos
Resumen comparativo de rendimiento por curso

📋 Sistema de Asistencia

Registro diario Lunes a Viernes (validación automática de días hábiles)
Estados: Presente o Ausente
Registro individual por alumno o masivo por curso completo
Historial visual con últimas clases marcadas
Reglas de aprobación combinadas (asistencia + nota):

Asistencia ≥ 80% + Nota ≥ 4.5 → ✅ Aprobado
Asistencia 70%–80% + Nota ≥ 5.0 → ✅ Aprobado
Resto de casos → ❌ Reprobado
Barras de progreso con marcadores visuales en 70% y 80%

📄 Informes Académicos

Informe completo por alumno con datos personales, notas y asistencia
Exportación a PDF profesional con ReportLab (tabla de notas, resumen, firmas)
Código de colores por estado de aprobación en el PDF
Descarga directa desde el navegador

📝 Observaciones

Registro de observaciones por alumno con 4 categorías: Académica, Conductual, Familiar y Médica
Fecha automática y registro del usuario que escribe la observación
Historial completo con opción de eliminar
Incluidas en el informe PDF

👨‍👩‍👧 Módulo de Apoderados

Ficha completa del apoderado: nombre, RUT, teléfono, correo, dirección, relación con el alumno y datos adicionales
Un apoderado por alumno (relación OneToOne)
Vista de ficha que incluye resumen académico del alumno asociado
Acceso directo al informe completo de notas

💬 Canal de Comunicación Apoderado–Profesor

Formulario interno con 5 categorías: Académico, Conductual, Administrativo, Salud y Otro
Notificación automática por correo al profesor jefe al recibir un mensaje
Sistema de respuestas con notificación al apoderado por correo
Gestión de estados: Pendiente, Respondido y Cerrado
Bandeja de mensajes con filtros por estado
Historial completo de conversaciones en la ficha del apoderado

🤖 Predicciones con Machine Learning

Algoritmo Random Forest (100 estimadores) con scikit-learn
Evalúa promedio y edad para predecir nivel de riesgo académico
Niveles: 🟢 Bajo, 🟡 Medio, 🔴 Alto
Probabilidad de riesgo expresada en porcentaje con barra visual
Recomendaciones personalizadas para cada alumno
El modelo se re-entrena automáticamente con los datos actuales

🎨 Diseño y UX

Tema oscuro corporativo con paleta navy y dorado
Glassmorphism en tarjetas y tablas
Fuentes tipográficas: Playfair Display (títulos) y DM Sans (cuerpo)
Animaciones y transiciones CSS
Diseño 100% responsive
Mensajes de éxito/error flotantes con auto-cierre
Gráfico doughnut en el dashboard (Chart.js)
Reloj en tiempo real en el panel de inicio
Scrollbar personalizada

🔐 Autenticación

Login y logout con django.contrib.auth
Todas las vistas protegidas con @login_required
Enlace al panel de administración solo para superusuarios


🛠️ Tecnologías Utilizadas
TecnologíaVersiónUsoPython3.14Lenguaje principalDjango6.0.2Framework webSQLite—Base de datosTailwind CSSCDNEstilos y diseñoChart.jsCDNGráficos en dashboardscikit-learnLatestMachine LearningpandasLatestManipulación de datosReportLabLatestGeneración de PDFGoogle FontsCDNTipografías


🚀 Instalación y Configuración
Requisitos previos

Python 3.10 o superior
pip
Git

Pasos de instalación

1. Clonar el repositorio
bashgit clone https://github.com/tu-usuario/App_Gestion_Escolar.git
cd App_Gestion_Escolar

3. Crear y activar el entorno virtual
bash# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python -m venv .venv
source .venv/bin/activate

3. Instalar dependencias
bashpip install django
pip install scikit-learn pandas
pip install reportlab

5. Aplicar migraciones
bashpy manage.py makemigrations
py manage.py migrate

7. Crear superusuario
bashpy manage.py createsuperuser

9. Iniciar el servidor
bashpy manage.py runserver

11. Acceder al sistema
http://127.0.0.1:8000/
Configuración de correo electrónico (opcional)
Para activar las notificaciones por correo entre apoderados y profesores, agrega esto en settings.py:
pythonEMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = 'tu_correo@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña_de_app'
DEFAULT_FROM_EMAIL  = 'Liceo Municipal <tu_correo@gmail.com>'

💡 Para Gmail es necesario activar la verificación en dos pasos y generar una contraseña de aplicación desde la configuración de seguridad de tu cuenta Google.

📦 Módulos del Sistema
URLs disponibles
MóduloURL baseDescripciónInicio/Dashboard con estadísticas y gráficoAlumnos/alumnos/CRUD completo de estudiantesProfesores/profesores/CRUD planta docenteCursos/cursos/CRUD de cursosNotas/notas/Notas, asistencia e informesApoderados/apoderados/Fichas y comunicaciónPredicciones/predicciones/Panel de riesgo académico MLAdmin/admin/Panel de administración Django
Modelos principales
python# Alumno
nombre, apellido, edad, correo, curso, promedio

# Profesor
nombre, especialidad, años_experiencia

# Curso
nombre_ramo, nivel, jornada, profesor_jefe (FK)

# Nota
alumno (FK), asignatura, nota_1, nota_2, nota_3, nota_4

# Asistencia
alumno (FK), asignatura, fecha, estado

# Observacion
alumno (FK), categoria, texto, fecha, usuario (FK)

# Apoderado
alumno (OneToOne), nombre, rut, relacion,
telefono, correo, direccion, datos_adicionales

# MensajeApoderado
apoderado (FK), categoria, asunto, mensaje,
respuesta, estado, fecha_envio, fecha_respuesta

🤖 Machine Learning
El módulo de predicciones utiliza un modelo de Random Forest entrenado dinámicamente con los datos del sistema en cada consulta.

Se extraen todos los alumnos con promedio registrado
Se construye un dataset con features: promedio y edad
Se etiqueta como "en riesgo" si el promedio es menor a 5.5
Se entrena un RandomForestClassifier con 100 estimadores
Se predice la probabilidad de riesgo para cada alumno
Se clasifica en tres niveles: Bajo, Medio y Alto

Niveles de riesgo
ProbabilidadNivelAcción recomendada< 30%🟢 BajoSeguimiento normal30% – 60%🟡 MedioRefuerzo preventivo> 60%🔴 AltoIntervención urgente

