from sqlalchemy import Column, DateTime, Integer, String, Date, DECIMAL
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base


# Definir la base para los modelos
Base = declarative_base()

# Modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False)