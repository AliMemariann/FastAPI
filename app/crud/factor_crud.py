from sqlalchemy.orm import Session
from app.models import Factors
from app.schemas import FactorCreate
from app.utils import date_converter


# ================== CREATE ====================
def create_Factor(db : Session, newFactor : FactorCreate):
    obj = Factors(
        cid = newFactor.cid,
        total = 0,
        jalalidate = date_converter.Today()
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


# ================== READ ====================
def get_Factor_by_id(db: Session, MyId: int):
    return db.get(Factors, MyId)

def get_Factor_by_cid(db: Session, MyCid: int):
    return db.query(Factors).filter(Factors.Cid == MyCid).all()

def get_Factors(db: Session):
    return db.query(Factors).all()


# ================== UPDATE ====================
def update_Factor(db: Session, MyId: int, total: int):
    obj = db.get(Factors, MyId)

    if obj:
        obj.total = total
        db.commit()
        db.refresh(obj)
    return obj


# ================== DELETE ====================
def delete_Factor_by_id(db: Session, MyId: int):
    obj = db.get(obj, MyId)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def delete_all_Factors(db: Session):
    DelCount = db.query(Factors).delete()
    db.commit()
    return DelCount
