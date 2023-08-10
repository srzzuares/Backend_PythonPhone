from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv
load_dotenv()
# una vez cargados los valores, podemos usarlos
API_KEY = os.getenv('SQL_SCRIPT')

engine = create_engine(API_KEY)
meta = MetaData()
conn = engine.connect()
