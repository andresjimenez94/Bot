import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class MarcaVehiculo(db.Base):

    __tablename__ = 'marcaVehiculo'
    id_marcaVehiculo = Column('id_marcaVehiculo', Integer, primary_key=True, autoincrement=True)
    nombre_marcaVehiculo = Column('nombre_marcaVehiculo', String(15), nullable=False)

    modelosVehiculo = relationship('ModeloVehiculo', back_populates='marcaVehiculo')

    def __init__(self,nombre_marcaVehiculo):
        self.nombre_marcaVehiculo = nombre_marcaVehiculo
    
    def __repr__(self):
        return f"<MarcaVehiculo {self.id_marcaVehiculo}>"