from pydantic import BaseModel, ConfigDict

class Factor_ItemBase(BaseModel):
    fid : int
    pid : int
    no : int
    price : int

class Factor_ItemCreate(Factor_ItemBase):
    pass

class Factor_ItemOut(Factor_ItemBase):
    model_config = ConfigDict(from_attributes=True)
    id : int
    total : int

