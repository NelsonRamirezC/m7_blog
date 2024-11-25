# password de todos los usuarios de prueba
Clavefacil*

## REQUISITOS PREVIOS A EJECUCIÓN DEL PROYECTO
1.- Crear entorno virtual
2.- Activar entorno virtual: ./venv/Script/Activate
3.- Instalar dependencias desde requirements.txt
    - ejecutar pip install -r requirements.txt

## RESTAURAR BASE DE DATOS

1.- Crear base de datos llamada proyecto_x_db
2.- restaurar desde archivo respaldo.tar

## EDITAR DATOS PARA BD EN SETTING.PY
Debe editar las credenciales de acceso a la base de datos
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "proyecto_x_db",
        "USER": "postgres",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
"""