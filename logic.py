import database.db as db
from models.MarcaVehiculo import MarcaVehiculo
from models.ModeloVehiculo import ModeloVehiculo
from models.TipoDocumento import TipoDocumento
from models.Dueno import Dueno
from models.Vehiculo import Vehiculo
from datetime import datetime
from sqlalchemy import extract

#################################################

def get_about_this(VERSION):
    response = (
        f"Simple Expenses Bot (pyTelegramBot) v{VERSION}"
        )
    
    return response

def get_help_message ():
    response = (
        "Estos son los comandos y órdenes disponibles:\n"
        "\n"
        "*/start* - Inicia la interacción con el bot (obligatorio)\n"
        "*/help* - Muestra este mensaje de ayuda\n"
        "*/about* - Muestra detalles de esta aplicación\n"
        "*/newtipodoc* - Crea yb nuevo tipo de documento\n"
        )

    return response

def get_welcome_message(bot_data):
    response = (
        f"Hola, soy *{bot_data.first_name}* "
        f"también conocido como *{bot_data.username}*.\n\n"
        "¡Estoy aquí para ayudarte!"
        )

    return response

def register_TipoDocumento(nombre_TipoDocumento):
    tipoDocumento = TipoDocumento(nombre_TipoDocumento)
    db.session.add(tipoDocumento)
    db.session.commit()
    return True

def List_TipoDocumento():
    tiposDocumentos = db.session.query(
			TipoDocumento
		).all()
    db.session.commit()
    return tiposDocumentos
    
def register_marca(nombre_marca):
    marcaVehiculo = MarcaVehiculo(nombre_marca)
    db.session.add(marcaVehiculo)
    db.session.commit()
    return True

def List_Marcar():
    marcasVehiculos = db.session.query(
			MarcaVehiculo
		).all()
    db.session.commit()
    return marcasVehiculos

def register_modelo(nombre_modeloVehiculo,id_marcaVehiculo):
    modeloVehiculo = ModeloVehiculo(nombre_modeloVehiculo,id_marcaVehiculo)
    db.session.add(modeloVehiculo)
    db.session.commit()
    return True

def register_dueno(nombre_dueno,numero_Documento_dueno,direccion_dueno,telefono_dueno,correo_dueno,id_tipoDocumento):
    dueno = Dueno(nombre_dueno,numero_Documento_dueno,direccion_dueno,telefono_dueno,correo_dueno,id_tipoDocumento)
    db.session.add(dueno)
    db.session.commit()
    return True

def List_Modelo_por_Marca(id_marcaVehiculo):
    modeloVehiculo = db.session.query(
			ModeloVehiculo
		).filter_by(
            id_marcaVehiculo = id_marcaVehiculo
        ).all()
    db.session.commit()
    return modeloVehiculo

def get_id_dueno(id_tipoDocumento,numero_Documento_dueno):

    dueno = db.session.query(
            Dueno
        ).filter_by(
            id_tipoDocumento = id_tipoDocumento
        ).filter_by(
            numero_Documento_dueno = numero_Documento_dueno
        ).first()

    if dueno == None:
        return 0
    
    return dueno.id_dueno

def register_vehiculo(placa_Vehiculo,id_modeloVehiculo,id_dueno):
    vehiculo = Vehiculo(placa_Vehiculo,id_modeloVehiculo,id_dueno)
    db.session.add(vehiculo)
    db.session.commit()
    return True
    