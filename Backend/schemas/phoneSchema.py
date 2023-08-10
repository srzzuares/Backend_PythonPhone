from pydantic import BaseModel
from datetime import date


class PhoneModel(BaseModel):
    Marca: str = 'Polaroid'
    AndroidVersion: str = '8.0.0'
    Ram: int = 4
    Almacenamiento: int = 32
    Estado: bool = 1


class PhoneModelPut(BaseModel):
    Marca: str = 'Polaroid'
    AndroidVersion: str = '8.0.0'
    Ram: int = 4
    Almacenamiento: int = 32
    Estado: bool = 1
    FechaActualizacion: date
