from fastapi import APIRouter
from config.db import conn
from models.phoneModel import Phones
from schemas.phoneSchema import PhoneModel
Server = APIRouter()


#get all students 

@Server.get("/alumnos")
async def get_alumnos():
    return "Hola"




