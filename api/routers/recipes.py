from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import recipes as controller
from ..schemas import recipes as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Recipes'],
    prefix="/recipes"
)

# Create a new recipe
@router.post("/", response_model=schema.Recipe)
def create(request: schema.RecipeCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Get all recipes
@router.get("/", response_model=list[schema.Recipe])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Get a single recipe by ID
@router.get("/{item_id}", response_model=schema.Recipe)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

# Update a recipe by ID
@router.put("/{item_id}", response_model=schema.Recipe)
def update(item_id: int, request: schema.RecipeUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

# Delete a recipe by ID
@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
