from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Float
from config.db import meta,engine

Phones = Table('alumnos',meta,
                Column('idPh', Integer, primary_key=True),
                Column('Marca', String(255)),
                Column('Tipo', String(255)),
                Column('Ram', Integer),
                Column('Almacenamiento', Integer))
meta.create_all(engine)

