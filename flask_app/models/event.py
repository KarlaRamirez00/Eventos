from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #flash es e encargado de mostrar los mensajes

from datetime import datetime #me permite manipular fechas

class Event:
    def __init__(self, data):

        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.date = data["date"]
        self.details = data["details"]
        self.image = data["image"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        self.user_name = data["user_name"] #Columna extra al hacer una consulta JOIN


    #Metodo que crea un nuevo objeto de Evento
    @classmethod
    def create(cls, form):
        #form = {"name":"Examen de Python", "location":"Online", "date":"204-06-28"... "user_id": 1}
        query = "INSERT INTO eventos (name, location, date, details, image, user_id) VALUES (%(name)s, %(location)s, %(date)s, %(details)s, %(image)s, %(user_id)s);"
        return connectToMySQL('esquema_eventos').query_db(query, form) #Regresa el id del nuevo evento     

    #Metodo que muestra un objeto de Evento
    @classmethod
    def read_one(cls, data):
        #data ={"id": 1}
        query = "SELECT eventos.*, users.first_name as user_name FROM eventos JOIN users ON eventos.user_id = users.id WHERE eventos.id = %(id)s;"
        #Lista con 1 diccionario
        result = connectToMySQL('esquema_eventos').query_db(query, data) 
        event = cls(result[0]) #Objeto Event
        return event
    
    #Metodo que muestra un objeto de Evento
    #WHERE date >= CURDATE() -> Sólo eventos de hoy y del futuro
    #ORDER BY date ASC -> Ordena los eventos de manera ascendente
    @classmethod
    def read_all(cls):
        query = "SELECT eventos.*, users.first_name as user_name FROM eventos JOIN users ON eventos.user_id = users.id WHERE date >= CURDATE() ORDER BY date ASC;" # current date -> la fecha actual
        #Lista con 1 diccionario
        results = connectToMySQL('esquema_eventos').query_db(query) 
        eventos = [] #Objetos de Event
        for ev in results:
            eventos.append(cls(ev)) #ev = {diccionario con la ifo de BD}, cls(ev) : Crear el objeto Event, eventos.append(): el objeto event lo agrego a la lista
        return eventos
    
    @staticmethod
    def validate_event(form):
        #form = {"name":"Examen de Python", "location":"Online", "date":"204-06-28"... "user_id": 1}
        is_valid = True

        if len(form["name"]) < 3:
            flash("El nombre del evento debe tener al menos 3 caracteres", "evento")
            is_valid = False

        if len(form["location"]) < 3:
            flash("La ubicación del evento debe tener al menos 3 caracteres", "evento")
            is_valid = False

        if len(form["details"]) < 3:
            flash("Los detalles del evento debe tener al menos 3 caracteres", "evento")
            is_valid = False

        # Verificar si el campo de fecha está vacío
        if form["date"] == "":
            flash("Ingrese una fecha", "evento")
            is_valid = False
        else:
            try:
                # Intentar convertir la fecha ingresada a un objeto datetime
                fecha_obj = datetime.strptime(form["date"], '%Y-%m-%d')
                hoy = datetime.now()
                # Verificar si la fecha es en el pasado
                if hoy > fecha_obj:
                    flash("La fecha no puede ser en el pasado!", "evento")
                    is_valid = False
            except ValueError:
                # Manejar el caso en que la fecha no tenga un formato válido 
                #esto lo hice porque al no poner fecha, se me caía la página y me tiraba esto: ValueError: time data '' does not match format '%Y-%m-%d'
                flash("Formato de fecha no válido", "evento")
                is_valid = False    
            
        return is_valid #Regresa True o False
    
    #update
    @classmethod
    def update(cls, form):
        query = "UPDATE eventos SET name=%(name)s, location=%(location)s, date=%(date)s, details=%(details)s, user_id=%(user_id)s WHERE id=%(id)s;"
        return connectToMySQL('esquema_eventos').query_db(query, form) 

    #delete
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM eventos WHERE id = %(id)s;"
        return connectToMySQL('esquema_eventos').query_db(query, data)
    