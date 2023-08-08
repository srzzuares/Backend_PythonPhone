from pydantic import BaseModel
class PhoneModel(BaseModel):
    idPh : int
    Marca : str
    Tipo : str
    Ram : int
    Almacenamiento : int