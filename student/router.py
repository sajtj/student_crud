from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import StudentIn, StudentOut
from .models import Student
from config.database import get_db

router = APIRouter()

@router.post("/students/", status_code=status.HTTP_201_CREATED, response_model=StudentOut)
def create_student(request: StudentIn, db: Session = Depends(get_db)):
    db_student = Student(**request.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/", status_code=status.HTTP_200_OK, response_model=list[StudentOut])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_students = db.query(Student).offset(skip).limit(limit).all()
    return db_students

@router.get("/students/{id}", status_code=status.HTTP_200_OK, response_model=StudentOut)
def read_student(id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.put("/students/{id}", status_code=status.HTTP_200_OK, response_model=StudentOut)
def update_student(id: int, request: StudentIn, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in request.model_dump().items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"msg": f"Student with ID {id} has been deleted successfully"}
