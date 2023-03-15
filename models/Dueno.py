import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class Dueno(db.Base):

    __tablename__ = 'dueno'
    id_dueno = Column('id_dueno', Integer, primary_key=True, autoincrement=True)
    nombre_dueno = Column('nombre_dueno', String(15), nullable=False)
    numero_Documento_dueno = Column('numero_Documento_dueno', String(15), nullable=False)
    direccion_dueno = Column('direccion_dueno', String(15), nullable=True)
    telefono_dueno = Column('telefono_dueno', String(15), nullable=True)
    correo_dueno = Column('correo_dueno', String(15), nullable=True)

    id_tipoDocumento = Column('id_tipoDocumento', Integer, ForeignKey('tipoDocumento.id_tipoDocumento',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    tipoDocumento = relationship("TipoDocumento", back_populates="duenos")
    


    vehiculos = relationship('Vehiculo', back_populates='dueno')

    def __init__(self,nombre_dueno,numero_Documento_dueno,direccion_dueno,telefono_dueno,correo_dueno,id_tipoDocumento):
        self.nombre_dueno = nombre_dueno
        self.numero_Documento_dueno = numero_Documento_dueno
        self.direccion_dueno = direccion_dueno
        self.telefono_dueno = telefono_dueno
        self.correo_dueno = correo_dueno
        self.id_tipoDocumento = id_tipoDocumento


    
    def __repr__(self):
        return f"<Dueno {self.id_dueno}>"