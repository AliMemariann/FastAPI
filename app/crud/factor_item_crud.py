from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from app.models import Factor_item
from app.schemas import Factor_ItemCreate


# ================== CREATE ====================
def create_Factor_item(db : Session, newFactor_item : Factor_ItemCreate):
    obj = Factor_item(
        fid = newFactor_item.fid,
        pid = newFactor_item.pid,
        no = newFactor_item.no,
        price = newFactor_item.price,
        total = newFactor_item.no * newFactor_item.price
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


# ================== READ ====================
def get_Factor_Item_by_id(db: Session, MyId: int):
    return db.get(Factor_item, MyId)

def get_Factor_Item_by_fid(db: Session, MyFid: int):
    sql = select(Factor_item).where(Factor_item.fid == MyFid)
    return db.scalars(sql).all()

def get_Factor_Items(db: Session):
    sql = select(Factor_item)
    return db.scalars(sql).all()


# ================== UPDATE ====================
def update_Factor_Item(db: Session, MyId: int, updated_Factor_Item: Factor_ItemCreate):
    obj = db.get(Factor_item, MyId)

    if obj:
        obj.no = updated_Factor_Item.no
        obj.price = updated_Factor_Item.price
        obj.total = updated_Factor_Item.no * updated_Factor_Item.price
        db.commit()
        db.refresh(obj)
    return obj


# ================== DELETE ====================
def delete_Factor_Item_by_id(db: Session, MyId: int):
    obj = db.get(Factor_item, MyId)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def delete_Factor_Item_by_fid(db: Session, MyFid: int):
    sql = delete(Factor_item).where(Factor_item.fid == MyFid)
    result = db.execute(sql)

    db.commit()
    return result.rowcount

def delete_all_Factor_Items(db: Session):
    sql = delete(Factor_item)
    result = db.execute(sql)

    db.commit()
    return result.rowcount