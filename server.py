# Pasos en la Terminal para ejecutar el proyecto:
# 1) Instalar las dependencias necesarias para el proyecto
#    pipenv install flask pymysql flask-bcrypt cryptography
# 2) Activar el entorno virtual de pipenv
#    pipenv shell
# 3) Ejecutar el servidor de la aplicación
#    python server.py

"""Servidor principal para ejecutar la aplicación Flask."""

# Importar la app
from flask_app import app

# Importar controladores (puede ser más de uno)
from flask_app.controllers import users_controller, events_controller # pylint: disable=unused-import

# Ejecución app
if __name__ == "__main__":
    app.run(debug=True)
