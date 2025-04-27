📋 Instrucciones para ejecutar el proyecto "Eventos"

➡️ Si es la primera vez que descargas el proyecto:

Instala pipenv si no lo tienes:

	pip install pipenv

Instala las dependencias necesarias:

	pipenv install flask pymysql flask-bcrypt cryptography

Activa el entorno virtual:

	pipenv shell

Ejecuta el servidor:

	python server.py


➡️ Si ya habías ejecutado el proyecto antes:

Activa el entorno virtual:

	pipenv shell

Ejecuta el servidor:

	python server.py

🛠️ Notas importantes:

Cada vez que cierres y vuelvas a abrir tu terminal o VS Code, debes reactivar el entorno virtual usando pipenv shell antes de correr el servidor.

Si ves errores de librerías faltantes, puedes instalarlas usando:

	pipenv install nombre_libreria

Para salir del entorno virtual:

exit

✨ Proyecto desarrollado usando:

	Python 3

	Flask

	pipenv

	PyMySQL

	flask-bcrypt

	cryptography


🛢️ Configuración de Base de Datos

1. Crear una base de datos en MySQL:
   - Nombre sugerido: eventos_db

2. Crear las tablas necesarias:
   - Ejecutar el script ubicado en flask_app/bd/scrip_eventos.sql

3. Configurar la conexión en el archivo flask_app/config/mysqlconnection.py:
   - Definir el host, usuario, contraseña y nombre de base de datos correctamente.

Ejemplo de configuración:
connection = pymysql.connect(host = 'localhost',
                                    user = 'root', # Cambia si usas otro usuario
                                    password = '', # Agrega aquí tu contraseña de MySQL si es necesario
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)

Notas:
- El servidor de MySQL debe estar ejecutándose.
- Asegúrate de que las credenciales sean correctas según tu entorno local.


🔗 Autor

	Karla Ramírez
	