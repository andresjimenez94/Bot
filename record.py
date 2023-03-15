class Record():
    id_marca = None
    tipo_documento = None
    num_documento = None
    nombre_dueño = None
    direccion_dueño = None
    telefono_dueno = None
    correo_dueno = None
    id_modelo = None
    placa = None
    id_dueno = None

    def set_user_data(self, id_marca,tipo_documento,num_documento,nombre_dueño,direccion_dueño,telefono_dueno,correo_dueno,id_modelo,placa,id_dueno):
        self.id_marca = id_marca
        self.tipo_documento = tipo_documento
        self.num_documento = num_documento
        self.nombre_dueño = nombre_dueño
        self.direccion_dueño = direccion_dueño
        self.telefono_dueno = telefono_dueno
        self.correo_dueno = correo_dueno
        self.id_modelo = id_modelo
        self.placa = placa
        self.id_dueno = id_dueno
