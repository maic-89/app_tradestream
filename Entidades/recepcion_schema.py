from pydantic import BaseModel
from datetime import date

class RecepcionCreate(BaseModel):
    embarque_id: int
    fecha_recepcion: date
    