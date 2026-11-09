from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
import app.crud as crud 
from app.schemas import CustomerCreate, CustomerOut

router = APIRouter(
    prefix= '/Customer',
    tags= ['This is Customer route']
)


# ================== CREATE ====================
@router.post('/', response_model= CustomerOut)
def create_customer(inCustomer: CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db = db, newCustomer = inCustomer)


# ================== READ ====================
@router.get('/id/{myid}', response_model= CustomerOut)
def get_customer_by_id(MyId: int, db: Session = Depends(get_db)):
    customer = crud.get_customer_by_id(db = db, MyId = MyId)
    if customer:
        return customer
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Customer with id {MyId} not found') 

@router.get('/username/{myuserame}', response_model= list[CustomerOut])
def get_customer_by_UserName(MyUserName: str, db: Session = Depends(get_db)):
    return crud.get_customer_by_UserName(db, MyUserName) or []

@router.get('/', response_model= list[CustomerOut])
def get_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db = db) or []


# ================== UPDATE ====================
@router.put('/update', response_model= CustomerOut)
def update_customer(MyId: int, InCustomer: CustomerCreate, db: Session = Depends(get_db)):
    customer = crud.update_customer(db = db, MyId = MyId, Ucustomer = InCustomer)

    if customer:
        return customer
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Customer with username {MyId} not found')       

@router.put('/toggle', response_model= CustomerOut)
def update_customer_toggle_active(MyId: int, InCustomer: CustomerCreate, db: Session = Depends(get_db)):
    customer = crud.update_customer_toggle_active(db = db, MyId = MyId)

    if customer:
        return customer
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Customer with username {MyId} not found') 


# ================== DELETE ====================
@router.delete('/id/{myid}', response_model= CustomerOut)
def delete_customer_by_id(MyId: int, db: Session = Depends(get_db)):
    customer = crud.delete_customer_by_id(db = db, MyId = MyId)

    if customer:
        return customer
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Customer with username {MyId} not found') 

@router.delete('/')
def delete_all_customers(db: Session = Depends(get_db)):
    DelCount = crud.delete_all_customers(db = db)
    return {'Deleted Customers Count': DelCount}