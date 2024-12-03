from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import customers as model
from sqlalchemy.exc import SQLAlchemyError

# Create a new customer
def create(db: Session, request):
    new_customer = model.Customers(
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address
    )

    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_customer


def read_all(db: Session):
    try:
        return db.query(model.Customers).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, item_id: int):
    try:
        customer = db.query(model.Customers).filter(model.Customers.id == item_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return customer


def update(db: Session, item_id: int, request):
    try:
        customer = db.query(model.Customers).filter(model.Customers.id == item_id)
        if not customer.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
        update_data = request.dict(exclude_unset=True)
        customer.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return customer.first()


def delete(db: Session, item_id: int):
    try:
        customer = db.query(model.Customers).filter(model.Customers.id == item_id)
        if not customer.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")
        customer.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return "Customer deleted successfully"