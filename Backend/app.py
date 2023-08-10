from fastapi import FastAPI
from routes.phoneRouter import Server
app = FastAPI()


app.include_router(Server, tags=["Tabla Celular"])
