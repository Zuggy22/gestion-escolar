Características

🔐 Login y logout con autenticación nativa de Django
👩‍🎓 Gestión de Alumnos, Profesores y Cursos
📝 Formularios de registro con validación
🎨 Diseño institucional con plantilla maestra compartida


🚀 Instalación

# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/App_Gestion_Escolar.git
cd App_Gestion_Escolar

# 2. Activar entorno virtual
.venv\Scripts\activate

# 3. Instalar dependencias
py -m pip install -r requirements.txt

# 4. Crear base de datos y superusuario
py manage.py migrate
py manage.py createsuperuser

# 5. Ejecutar servidor
py manage.py runserver
Abre http://127.0.0.1:8000/ en tu navegador 🎉

