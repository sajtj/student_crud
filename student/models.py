from sqlalchemy import Column, Integer, String, Date, Enum
from config.database import Base
import enum

class GenderEnum(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    last_name = Column(String(255), index=True, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    degree = Column(String(255), nullable=False)
    date_of_registration = Column(Date, nullable=False)
    graduation_date = Column(Date, nullable=False)
    address = Column(String(255), nullable=False)
    contact_number = Column(String(15), nullable=False) 