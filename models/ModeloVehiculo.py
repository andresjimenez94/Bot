import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class ModeloVehiculo(db.Base):

    __tablename__ = 'modeloVehiculo'
    id_modeloVehiculo = Column('id_modeloVehiculo', Integer, primary_key=True, autoincrement=True)
    nombre_modeloVehiculo = Column('nombre_modeloVehiculo', String(15), nullable=False)

    id_marcaVehiculo = Column('idMarcaVehiculo', Integer, ForeignKey('marcaVehiculo.id_marcaVehiculo',
    onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    marcaVehiculo = relationship('MarcaVehiculo', back_populates='modelosVehiculo')

    vehiculos = relationship('Vehiculo', back_populates='modeloVehiculo')

    

    def __init__(self,nombre_modeloVehiculo,id_marcaVehiculo):
        self.nombre_modeloVehiculo = nombre_modeloVehiculo
        self.id_marcaVehiculo = id_marcaVehiculo
    
    def __repr__(self):
        return f"<ModeloVehiculo {self.id_modeloVehiculo}>"