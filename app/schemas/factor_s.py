from pydantic import BaseModel, ConfigDict
from datetime import datetime


class FactorBase(BaseModel):
    cid : int

class FactorCreate(FactorBase):
    pass

class FactorOut(FactorBase):
    model_config = ConfigDict(from_attributes=True)
    id : int
    date : datetime
    total : int
    jalalidate : str
