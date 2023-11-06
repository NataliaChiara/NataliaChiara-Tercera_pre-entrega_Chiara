# nuevo-django

1 - Crear entorno virtual (SOLO LA PRIMERA VEZ)

    python -m venv env

2 - Correr entorno virtual

    . env/Scripts/activate (desactivarlo con "deactivate")  

3 - Instalar Django y dependencias (SOLO LA PRIMERA VEZ)

    pip install Django

    pip install -r requirements.txt

4 - Gestionar la migracion de datos (SOLO LA PRIMERA VEZ)

    python manage.py migrate

5 - Correr el servidor 

    python manage.py runserver

---------------------------------------------------------

Se accede al sitio a traves de

    http://127.0.0.1:8000/

Si se agrega alguna dependencia, actualizar el requirements.txt con el comando

    pip freeze > requirements.txt

Si se va a realizar algun cambio abrir una rama

    feature/*nombre del cambio*

Para agregar un super-usuario

    python manage.py createsuperuser
    (usuario: natalia, contraseña: 12345678)

Despues de hacer cambios en los modelos, agregar en admin.py

    1 - from django.contrib import admin
        from inicio.models import *MODELO*

        admin.site.register(*MODELO*) (uno a la vez)

    2- Correr comandos
        python manage.py makemigrations
        python manage.py migrate