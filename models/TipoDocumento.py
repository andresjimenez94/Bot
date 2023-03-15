import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class TipoDocumento(db.Base):

    __tablename__ = 'tipoDocumento'
    id_tipoDocumento = Column('id_tipoDocumento', Integer, primary_key=True, autoincrement=True)
    nombre_tipoDocumento = Column('nombre_tipoDocumento', String(15), nullable=False)

    duenos = relationship('Dueno', back_populates='tipoDocumento')

    def __init__(self, nombre_tipoDocumento=""):
        self.nombre_tipoDocumento = nombre_tipoDocumento
    
    def __repr__(self):
        return f"<tipoDocumento {self.id_tipo_documento}>"