from fastapi import APIRouter
from config.db import conn
from controllers.phoneController import get_Alls, get_One, get_create, get_update, get_deleteStatus, get_delete
from schemas.phoneSchema import PhoneModel, PhoneModelPut
Server = APIRouter()


# get all students

@Server.get("/phone/get_All")
def GET_ALL():
    return get_Alls()


@Server.get("/phone/{idPh}")
def GET_ONE(idPh):
    return get_One(idPh)


@Server.post("/phone/insert")
def POST_phone(data: PhoneModel):
    return get_create(data)


@Server.put("/phone/update/{idPh}")
def PUT_phone(data: PhoneModelPut, idPh):
    return get_update(data, idPh)


@Server.delete("/phone/deleteSt/{idPh}")
def DEL_phoneSTATUS(idPh):
    return get_deleteStatus(idPh)


@Server.delete("/phone/delete/{idPh}")
def DEL_phone(idPh):
    return get_delete(idPh)
