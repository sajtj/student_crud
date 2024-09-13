from pydantic import BaseModel
from datetime import date


class StudentBase(BaseModel):
    name: str
    last_name: str
    gender: str
    date_of_birth: date
    degree: str
    date_of_registration: date
    graduation_date: date
    address: str
    contact_number: str

class StudentIn(StudentBase):
    pass
        
class StudentOut(StudentBase):
    id: int
    class Config:
        from_attributes = True
