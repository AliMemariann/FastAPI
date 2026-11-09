from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from app.models import Product
from app.schemas import ProductCreate


# ================== CREATE ====================
def create_Product(db : Session, newProduct : ProductCreate):
    obj = Product(
        name = newProduct.name,
        price = newProduct.price
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


# ================== READ ====================
def get_Product_by_id(db: Session, MyId: int):
    return db.get(Product, MyId)

def get_Product_by_name(db: Session, MyName: str):
    sql = select(Product).where(Product.name == MyName).order_by(Product.name)
    return db.scalars(sql).all()

def get_Product_by_price(db: Session, MyPrice: int):
    return db.query(Product).filter(Product.pricerice == MyPrice).all()

def get_Products(db: Session):
        sql = select(Product).order_by(Product.name)
        return db.scalars(sql).all()


# ================== UPDATE ====================
def update_Product(db: Session, MyId: int, updated_Product: ProductCreate):
    obj = db.get(Product, MyId)

    if obj:
        obj.name = updated_Product.name
        obj.price = updated_Product.price
        db.commit()
        db.refresh(obj)
    return obj


# ================== DELETE ====================
def delete_Product_by_id(db: Session, MyId: int):
    obj = db.get(obj, MyId)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def delete_all_Products(db: Session):
    DelCount = db.query(Product).delete()
    db.commit()
    return DelCount