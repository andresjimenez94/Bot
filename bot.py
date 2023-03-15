#########################################################

from config import bot
import config
from time import sleep
import re
import logic
import database.db as db

from record import Record
record = Record()

#########################################################

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)

#########################################################

@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(
        message.chat.id,
        logic.get_welcome_message(bot.get_me()),
        parse_mode="Markdown")
    
    bot.send_message(
        message.chat.id,
        logic.get_help_message(),
        parse_mode="Markdown")

#########################################################

@bot.message_handler(commands=['help'])
def on_command_help(message):
    pass

#########################################################

@bot.message_handler(commands=['about'])
def on_command_about(message):
    pass

#########################################################
@bot.message_handler(commands=['newtipodoc'])
def on_command_start(message):
    response = bot.reply_to(message, "Ingresa el Nombre del Nuevo tipo de Documento")
    bot.register_next_step_handler(response, process_new_tipo_doc)

def process_new_tipo_doc(message):
    try:
        message.text
        logic.register_TipoDocumento(message.text)
        bot.reply_to(message, f"Se Guardó con exito")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

#########################################################
@bot.message_handler(commands=['listtipodoc'])
def on_command_start(message):
     process_List_tipo_doc(message)
    

def process_List_tipo_doc(message):
    try:
        text = ""
        tiposDocumentos = logic.List_TipoDocumento ()
        if not tiposDocumentos:
            text = f"No tienes Tipos de documentos registrados"
        else:
            for e in tiposDocumentos: 
                text += f"{e.id_tipoDocumento} - {e.nombre_tipoDocumento} \n"
        
        bot.reply_to(message, text, parse_mode="Markdown")

    except Exception as e:
         bot.reply_to(message, f"Algo terrible sucedió: {e}")

#########################################################
@bot.message_handler(commands=['newmarca'])
def on_command_start(message):
    response = bot.reply_to(message, "Ingresa el Nombre de la Nueva marca de vehiculo")
    bot.register_next_step_handler(response, process_new_marca)

def process_new_marca(message):
    try:
        message.text
        logic.register_marca(message.text)
        bot.reply_to(message, f"Se Guardó con exito")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

#########################################################
def process_List_marcas(message):
    try:
        text = ""
        marcasVehiculos = logic.List_Marcar ()
        if not marcasVehiculos:
            text = f"No tienes Tipos de Marcar registradas"
        else:
            for e in marcasVehiculos: 
                text += f"{e.id_marcaVehiculo} - {e.nombre_marcaVehiculo} \n"
        
        bot.reply_to(message, text, parse_mode="Markdown")

    except Exception as e:
         bot.reply_to(message, f"Algo terrible sucedió: {e}")

#########################################################
@bot.message_handler(commands=['newmodelo'])
def on_command_start(message):
    response = bot.reply_to(message, "Seleccione la marca del nuevo modelo")
    text = ""
    marcasVehiculos = logic.List_Marcar ()
    if not marcasVehiculos:
        text = f"No tienes Tipos de Marcar registradas"
    else:
        for e in marcasVehiculos: 
            text += f"{e.id_marcaVehiculo} - {e.nombre_marcaVehiculo} \n"
    
    response = bot.reply_to(message, text)
    bot.register_next_step_handler(response, process_nombre_new_modelo)

def process_nombre_new_modelo(message):
    try:
        id_marca = int(message.text)
        record.id_marca = id_marca
        response = bot.reply_to(message, "Nombre del nuevo modelo")
        bot.register_next_step_handler(response, process_new_modelo)
    
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def process_new_modelo(message):
    try:
        message.text
        logic.register_modelo(message.text,record.id_marca)
        bot.reply_to(message, f"Se Guardó con exito")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

#########################################################
@bot.message_handler(commands=['newdueno'])
def on_command_start(message):
    response = bot.reply_to(message, "Seleccione tipo de documento del Nuevo dueño")
    text = ""
    tiposDocumentos = logic.List_TipoDocumento ()
    if not tiposDocumentos:
        text = f"No tienes Tipos de documentos registrados"
    else:
        for e in tiposDocumentos: 
            text += f"{e.id_tipoDocumento} - {e.nombre_tipoDocumento} \n"
    
    response = bot.reply_to(message, text)
    bot.register_next_step_handler(response, process_num_doc_new_dueño)

def process_num_doc_new_dueño(message):
    try:
        tipo_documento = int(message.text)
        record.tipo_documento = tipo_documento
        response = bot.reply_to(message, "numero documento del nuevo dueño")
        bot.register_next_step_handler(response, process_nombre_new_dueño)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def process_nombre_new_dueño(message):
    try:
        num_documento = message.text
        record.num_documento = num_documento

        record.id_dueno = logic.get_id_dueno(record.tipo_documento,record.num_documento)

        if record.id_dueno != 0:
             bot.reply_to(message, f"Dueño Ya existe")
             return

        response = bot.reply_to(message, "Nombre del nuevo dueño")
        bot.register_next_step_handler(response, process_direccion_new_dueño)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def process_direccion_new_dueño(message):
    try:
        nombre_dueño = message.text
        record.nombre_dueño = nombre_dueño
        response = bot.reply_to(message, "dirección del nuevo dueño")
        bot.register_next_step_handler(response, process_telefono_new_dueño)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def process_telefono_new_dueño(message):
    try:
        direccion_dueño = message.text
        record.direccion_dueño = direccion_dueño
        response = bot.reply_to(message, "telefono del nuevo dueño")
        bot.register_next_step_handler(response, process_correo_new_dueño)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def process_correo_new_dueño(message):
    try:
        telefono_dueno = message.text
        record.telefono_dueno = telefono_dueno
        response = bot.reply_to(message, "correo del nuevo dueño")
        bot.register_next_step_handler(response, process_new_dueño)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def process_new_dueño(message):
    try:
        correo_dueno = message.text
        record.correo_dueno = correo_dueno
        logic.register_dueno(record.nombre_dueño,record.num_documento,record.direccion_dueño,record.telefono_dueno,record.correo_dueno,record.tipo_documento)
        bot.reply_to(message, f"Se Guardó con exito")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

#########################################################

@bot.message_handler(commands=['newvehiculo'])
def on_command_start(message):
    response = bot.reply_to(message, "Seleccione la marca del nuevo vehiculo")
    text = ""
    marcasVehiculos = logic.List_Marcar ()
    if not marcasVehiculos:
        text = f"No tienes Tipos de Marcar registradas"
    else:
        for e in marcasVehiculos: 
            text += f"{e.id_marcaVehiculo} - {e.nombre_marcaVehiculo} \n"
    
    response = bot.reply_to(message, text)
    bot.register_next_step_handler(response, process_modelo_new_vehiculo)

def process_modelo_new_vehiculo(message):
    id_marca = message.text
    record.id_marca = id_marca
    response = bot.reply_to(message, "Seleccione la modelo del nuevo vehiculo")
    text = ""
    modeloVehiculo = logic.List_Modelo_por_Marca (id_marca)
    if not modeloVehiculo:
        text = f"No tienes Modelos registrados"
    else:
        for e in modeloVehiculo: 
            text += f"{e.id_modeloVehiculo} - {e.nombre_modeloVehiculo} \n"
    
    response = bot.reply_to(message, text)
    bot.register_next_step_handler(response, process_tipo_doc_new_vehiculo)

def process_tipo_doc_new_vehiculo(message):
    id_modelo = int(message.text)
    record.id_modelo = id_modelo
    response = bot.reply_to(message, "Seleccione tipo de documento del dueño del nuevo vehiculo")
    text = ""
    tiposDocumentos = logic.List_TipoDocumento ()
    if not tiposDocumentos:
        text = f"No tienes Tipos de documentos registrados"
    else:
        for e in tiposDocumentos: 
            text += f"{e.id_tipoDocumento} - {e.nombre_tipoDocumento} \n"
    
    response = bot.reply_to(message, text)
    bot.register_next_step_handler(response, process_num_doc_new_vehiculo)

def process_num_doc_new_vehiculo(message):
    try:
        tipo_documento = message.text
        record.tipo_documento = tipo_documento
        response = bot.reply_to(message, "Numero de documento del dueño del nuevo vehiculo")
        bot.register_next_step_handler(response, process_placa_new_vehiculo)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def process_placa_new_vehiculo(message):
    try:
        num_documento = message.text
        record.num_documento = num_documento
        record.id_dueno = logic.get_id_dueno(record.tipo_documento,record.num_documento)

        if record.id_dueno == 0:
             bot.reply_to(message, f"Dueño no existe")
             return

        response = bot.reply_to(message, "placa del nuevo vehiculo")
        bot.register_next_step_handler(response, process_new_vehiculo)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def process_new_vehiculo(message):
    try:
        placa = message.text
        record.placa = placa
        logic.register_vehiculo(record.placa,record.id_modelo,record.id_dueno)
        bot.reply_to(message, f"Se Guardó con exito")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")


#########################################################


@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    pass

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=20)

#########################################################