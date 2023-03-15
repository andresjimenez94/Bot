import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class Vehiculo(db.Base):

    __tablename__ = 'vehiculo'
    id_marcaVehiculo = Column('id_Vehiculo', Integer, primary_key=True, autoincrement=True)
    placa_Vehiculo = Column('placa_Vehiculo', String(15), nullable=False)

    id_modeloVehiculo = Column('id_modeloVehiculo', String(15), ForeignKey('modeloVehiculo.id_modeloVehiculo',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    modeloVehiculo = relationship('ModeloVehiculo', back_populates='vehiculos')

    id_dueno = Column('id_dueno', String(15), ForeignKey('dueno.id_dueno',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    dueno = relationship('Dueno', back_populates='vehiculos')

    def __init__(self,placa_Vehiculo,id_modeloVehiculo,id_dueno):
        self.placa_Vehiculo = placa_Vehiculo
        self.id_modeloVehiculo = id_modeloVehiculo
        self.id_dueno = id_dueno
    
    def __repr__(self):
        return f"<vehiculo {self.id_Vehiculo}>"