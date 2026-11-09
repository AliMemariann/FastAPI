from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
import app.crud as crud 
from app.schemas import ProductCreate, ProductOut

router = APIRouter(
    prefix= '/Product',
    tags= ['This is Product route']
)


# ================== CREATE ====================
@router.post('/', response_model= ProductOut)
def creat_Product(inProduct: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_Product(db = db, newProduct = inProduct)


# ================== READ ====================
@router.get('/id/{myid}', response_model= ProductOut)
def get_Product_by_id(MyId: int, db: Session = Depends(get_db)):
    product = crud.get_Product_by_id(db = db, MyId = MyId)
    
    if product:
        return product
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Product with id {MyId} not found')

@router.get('/username/{myusername}', response_model= list[ProductOut])
def get_Product_by_name(db: Session = Depends(get_db)):
    return crud.get_Product_by_name(db = db)

@router.get('/price', response_model= list[ProductOut])
def get_Product_by_price( db: Session = Depends(get_db)):
    return crud.get_Product_by_price(db = db)

@router.get('/', response_model= list[ProductOut])
def get_Products(db: Session = Depends(get_db)):
    return crud.get_Products(db = db)


# ================== UPDATE ====================
@router.put('/update/{myid}', response_model= ProductOut)
def update_Product(MyId: int, inProduct: ProductCreate, db: Session = Depends(get_db)):
    product = crud.update_Product(db = db, MyId = MyId, updated_Product = inProduct)

    if product:
        return product
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Product with id {MyId} not found')


# ================== DELETE ====================
@router.delete('/id/{myid}', response_model= ProductOut)
def delete_Product_by_id(MyId: int, db: Session = Depends(get_db)):
    product = crud.delete_Product_by_id(db = db, MyId = MyId)

    if product:
        return product
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Product with Id {MyId} not found') 

@router.delete('/')
def delete_all_Products(db: Session = Depends(get_db)):
    DelCount = crud.delete_all_Products(db = db)
    return {'Deleted Products Count': DelCount}