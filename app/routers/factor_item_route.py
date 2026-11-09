from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
import app.crud as crud 
from app.schemas import Factor_ItemCreate, Factor_ItemOut

router = APIRouter(
    prefix= '/Factor Item',
    tags= ['This is Factor Item route']
)


# ================== CREATE ====================
@router.post('/', response_model= Factor_ItemOut)
def creat_Factor_item(inFactor_item: Factor_ItemCreate, db: Session = Depends(get_db)):
    return crud.create_Factor_item(db = db, newFactor_item = inFactor_item)


# ================== READ ====================
@router.get('/id/{myid}', response_model= Factor_ItemOut)
def get_Factor_Item_by_id(MyId: int, db: Session = Depends(get_db)):
    factor_item = crud.get_Factor_by_id(db = db, MyId = MyId)
    
    if factor_item:
        return factor_item
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Factor Item with id {MyId} not found')

@router.get('/fid/{myfid}', response_model= list[Factor_ItemOut])
def get_Factor_Item_by_fid(MyFid: int, db: Session = Depends(get_db)):
    return crud.get_Factor_Item_by_fid(db = db, MyFid = MyFid)

@router.get('/', response_model= list[Factor_ItemOut])
def get_Factor_Items(db: Session = Depends(get_db)):
    return crud.get_Factor_Items(db = db)


# ================== UPDATE ====================
@router.put('/update/{myid}', response_model= Factor_ItemOut)
def update_Factor_Item(MyId: int, inFactor_item: Factor_ItemCreate, db: Session = Depends(get_db)):
    factor_item = crud.update_Factor_Item(db = db, MyId = MyId, updated_Factor_Item = inFactor_item)

    if factor_item:
        return factor_item
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Factor Item with id {MyId} not found') 


# ================== DELETE ====================
@router.delete('/delete/id/{myid}', response_model= Factor_ItemOut)
def delete_Factor_Item_by_id(MyId: int, db: Session = Depends(get_db)):
    factor_item = crud.delete_Factor_Item_by_id(db = db, MyId = MyId)

    if factor_item:
        return factor_item
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Factor item with id {MyId} not found') 

@router.delete('/delete/fid/{myfid}')
def delete_Factor_Item_by_fid(MyFid: int, db: Session = Depends(get_db)):
    factor_item = crud.delete_Factor_Item_by_fid(db = db, MyFid = MyFid)

    if factor_item:
        return factor_item
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Factor item with id {MyFid} not found') 

@router.delete('/')
def delete_all_Factor_Items(db: Session = Depends(get_db)):
    DelCount = crud.delete_all_Factor_Items(db = db)
    return {'Deleted Factors Count': DelCount}