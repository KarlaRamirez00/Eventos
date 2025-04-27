#BONUS**
#<3 Orden de Dashboard sea en base a fecha asc
#<3 Que en dashboard no aparezcan eventos en el pasado
#<3 Validar que el evento sea en el futuro
#<3 Almacenará el detalle en algún lado, para que si hay errores, no necesite volver a escribir todo de nuevo
#<3 Al editar, hacer un double check de que la persona de sesión sea el creador del evento
#PENDIENTE: Revisar que el nombre del evento sea único -> Validemos edición cambiará un poco

#Objetos: user.id
#Diccionarios: session["user_id"]
#Lista: result[0]

from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Importamos los modelos
from flask_app.models.event import Event
from flask_app.models.user import User

# Para nombre seguro de la imagen
from werkzeug.utils import secure_filename
#Para subir imágenes
from werkzeug.utils import secure_filename
import os

@app.route("/nuevo")
def nuevo():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    #Va a recibir el formulario... request.form = diccionario con toda la info del Formulario
    #Verificar que el usuario haya uiniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Guardamos en sesión los detalles del evento, por si hay error, para que no se pierda esta info y así no tener que escribir todo de nuevo.
    session["details"] = request.form["details"]
    #Validamos
    if not Event.validate_event(request.form):
        return redirect("/nuevo")
    
    # Revisamos que haya subido algo
    if 'image' not in request.files:
        flash("Ingrese la imagen", "evento")
        return redirect("/nuevo")

    # Revisamos que no esté vacío
    imagen = request.files["image"]
    if imagen.filename == '':
        flash("No seleccionó imagen", "evento")
        return redirect("/nuevo")
    
    nombre_imagen = secure_filename(imagen.filename)
    #guardar la imagen en una carpeta
    imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen))

    formulario = {"name": request.form['name'], "location": request.form['location'], "date": request.form['date'], "details": request.form['details'], "user_id": request.form['user_id'], "image": nombre_imagen}

        
    Event.create(formulario)
    session.pop("details") #Quitamos detalles de sesión, para que en un nuevo evento no aparezcan los del evento creado anteriormente.
    return redirect("/dashboard")

@app.route("/ver/<int:id>") #ver/1
def read(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    dicc = {"id" : id} #{"id" = 1}
    event = Event.read_one(dicc) #Invoco de la clase Event al método read_one(), enviamos el diccionario y recibimos un objeto Events
    return render_template("view.html", event=event)

@app.route("/borrar/<int:id>")  #/borrar/2
def delete(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Metodo que borra un registro en base a su ID
    dicc = {"id" : id}
    Event.delete(dicc)
    return redirect("/dashboard")

@app.route("/editar/<int:id>") #/editar/3
def edit(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    dicc = {"id" : id} #{"id" = 1}
    event = Event.read_one(dicc) #Invoco de la clase Event al método read_one(), enviamos el diccionario y recibimos un objeto Events. OJO! Aquí esto es para poder editar con los datos prepoblados.
    #Revisar que sí sea el usuario en sesión el mismo que creó el evento, para que lo pueda editar
    if session['user_id'] != event.user_id:
        return redirect("/dashboard")
    
    return render_template("edit.html", event=event)

@app.route("/update", methods=["POST"])
def update():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Recibir request.form = diccionario con la info del formulario
    #Validamos
    if not Event.validate_event(request.form):
        return redirect("/editar"+request.form["id"])
    
    Event.update(request.form)
    return redirect("/dashboard")
