from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name : str
    price : int
    
class ProductCreate(ProductBase):
    password_hash : str

class ProductOut(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id : int

