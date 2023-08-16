from config.db import conn
from models.phoneModel import PhonesModel
"""     
    http://127.0.0.1:8000/docs
    
    """


def get_Alls():
    listPhonesModel = conn.execute(PhonesModel.select()).fetchall()
    list = []
    for aut in listPhonesModel:
        dicci = {
            "idPh": aut[0],
            "Marca": aut[1],
            "AndroidVersion": aut[2],
            "Ram": aut[3],
            "Almacenamiento": aut[4],
            "Estado": aut[5],
            "FechaActualizacion": aut[6],
            "FechaRegistro": aut[7],
        }
        list.append(dicci)
    return list


def get_One(idPh):
    listOnePhonesModel = conn.execute(PhonesModel.select().where(
        PhonesModel.c.IdPh == idPh)).first()
    if listOnePhonesModel is not None:
        dicci = {
            "idPh": listOnePhonesModel[0],
            "Marca": listOnePhonesModel[1],
            "AndroidVersion": listOnePhonesModel[2],
            "Ram": listOnePhonesModel[3],
            "Almacenamiento": listOnePhonesModel[4],
            "Estado": listOnePhonesModel[5],
            "FechaActualizacion": listOnePhonesModel[6],
            "FechaRegistro": listOnePhonesModel[7],
        }
        return dicci
    else:
        res = {
            "status": "No existe el Celular"
        }
        return res


def get_create(data):
    conn.execute(PhonesModel.insert().values(dict(data)))
    conn.commit()
    res = {'message': "Celular Agregado"}
    return res


def get_update(data, idPh):
    ip = get_One(idPh)
    if ip.get("status") == "No existe el Celular":
        return ip
    else:
        result = conn.execute(PhonesModel.update().values(
            dict(data)).where(PhonesModel.c.IdPh == idPh))
        conn.commit()
        res = {"status": "Celular Actualizado"}
        return res


def get_deleteStatus(idPh):
    ip = get_One(idPh)
    if ip.get("status") == "No existe el Celular":
        return ip
    else:
        result = conn.execute(PhonesModel.update().values(Estado=0).where(
            PhonesModel.c.IdPh == idPh))
        conn.commit()
        res = {"status": "Celular desactivado"}
        return res


def get_delete(idPh):
    ip = get_One(idPh)
    if ip.get("status") == "No existe el Celular":
        return ip
    else:
        result = conn.execute(PhonesModel.delete().where(
            PhonesModel.c.IdPh == idPh))
        conn.commit()
        res = {"status": "Celular eliminado"}
        return res
