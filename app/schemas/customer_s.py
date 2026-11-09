from pydantic import BaseModel, ConfigDict
from .factor_s import FactorOut

class CustomerBase(BaseModel):
    username : str

class CustomerCreate(CustomerBase):
    password : str

class CustomerOut(CustomerBase):
    model_config = ConfigDict(from_attributes=True)
    id : int
    is_active : bool

    factors : list[FactorOut] = []