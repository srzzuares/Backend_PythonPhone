from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
import datetime
from config.db import meta, engine

PhonesModel = Table('phones', meta,
                    Column('IdPh', Integer, primary_key=True),
                    Column('Marca', String(45),
                           nullable=True, default='Polaroid'),
                    Column('AndroidVersion', String(45),
                           nullable=True, default='8.0.0'),
                    Column('Ram', Integer, nullable=True, default=4),
                    Column('Almacenamiento', Integer,
                           nullable=True, default=32),
                    Column('Estado', Boolean, nullable=True, default=1),
                    Column('FechaActualizacion', nullable=True,
                           default=datetime.datetime.utcnow),
                    Column('FechaRegistro', nullable=True, default=datetime.datetime.utcnow))
meta.create_all(engine)
