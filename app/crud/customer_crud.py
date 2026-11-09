from sqlalchemy.orm import Session
from app.models import Customer
from app.schemas import CustomerCreate
from app.utils import security


# ================== CREATE ====================
def create_customer(db : Session, newCustomer : CustomerCreate):
    obj = Customer(
        username = newCustomer.username,
        password_hash = security.hash_password(newCustomer.password)
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


# ================== READ ====================
def get_customer_by_id(db: Session, MyId: int):
    return db.get(Customer, MyId)

def get_customer_by_UserName(db: Session, MyUserName: str):
    return db.query(Customer).filter(Customer.username >= MyUserName).all()

def get_customers(db: Session):
    return db.query(Customer).all()


# ================== UPDATE ====================
def update_customer(db: Session, MyId: int, Ucustomer: CustomerCreate):
    obj = db.get(Customer, MyId)

    if obj:
        obj.username = Ucustomer.username
        obj.password_hash = security.hash_password(Ucustomer.password)
        db.commit()
        db.refresh(obj)
    return obj

def update_customer_toggle_active(db: Session, MyId: int):
    obj = db.get(Customer, MyId)

    if obj:
        obj.is_active = not obj.is_active
        db.commit()
        db.refresh(obj)
    return obj


# ================== DELETE ====================
def delete_customer_by_id(db: Session, MyId: int):
    obj = db.get(Customer, MyId)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def delete_all_customers(db: Session):
    DelCount = db.query(Customer).delete()
    db.commit()
    return DelCount