from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
import app.crud as crud 
from app.schemas import FactorCreate, FactorOut

router = APIRouter(
    prefix= '/Factor',
    tags= ['This is Factor route']
)


# ================== CREATE ====================
@router.post('/', response_model= FactorOut)
def creat_Fator(inFactor: FactorCreate, db: Session = Depends(get_db)):
    return crud.create_Factor(db = db, newFactor = inFactor)


# ================== READ ====================
@router.get('/id/{myid}', response_model= FactorOut)
def get_Factor_by_id(MyId: int, db: Session = Depends(get_db)):
    factor = crud.get_Factor_by_id(db = db, MyId = MyId)

    if factor:
        return factor
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Factor with id {MyId} not found')

@router.get('/cid/{mycid}', response_model= list[FactorOut])
def get_Factor_by_cid(MyCid: int, db: Session = Depends(get_db)):
    return crud.get_Factor_by_cid(db = db)

@router.get('/', response_model= list[FactorOut])
def get_Factors(db: Session = Depends(get_db)):
    return crud.get_Factors(db = db)


# ================== UPDATE ====================
@router.put('/update/{myid}', response_model= FactorOut)
def update_Factor(MyId: int, inTotal: int , db: Session = Depends(get_db)):
    factor = crud.update_Factor(db = db, MyId = MyId, total = inTotal)

    if factor:
        return factor
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Factor with id {MyId} not found') 


# ================== DELETE ====================
@router.delete('/delete/{myid}', response_model= FactorOut)
def delete_Factor_by_id(MyId: int, db: Session = Depends(get_db)):
    factor = crud.delete_Factor_by_id(db = db, MyId = MyId)

    if factor:
        return factor
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Factor with id {MyId} not found') 

@router.delete('/')
def delete_all_Factors(db: Session = Depends(get_db)):
    DelCount = crud.delete_all_Factors(db = db)
    return {'Deleted Factors Count': DelCount}

