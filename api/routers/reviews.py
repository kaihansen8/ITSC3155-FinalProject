from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..controllers import review as controller
from ..schemas.review import Review, ReviewCreate, ReviewUpdate
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Reviews"],
    prefix="/reviews"
)

@router.post("/", response_model=Review, status_code=status.HTTP_201_CREATED)
def create(request: ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[Review])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=Review)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=Review)
def update(item_id: int, request: ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, item_id=item_id, request=request)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)