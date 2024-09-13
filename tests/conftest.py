"""
    1- set your test database url in .env
    2- execute 'pytest -v --disable-warnings' command to run tests.
"""
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from config.database import get_db
from config.database import Base
from student.schemas import StudentOut
import pytest
import os

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
            
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    
@pytest.fixture
def test_student(client):
    student_data = {
    "name": "Sajad",
    "last_name": "Tajik",
    "gender": "Male",
    "date_of_birth": "2000-01-01",
    "degree": "Computer Science",
    "date_of_registration": "2023-09-12",
    "graduation_date": "2024-05-15",
    "address": "Khoone",
    "contact_number": "12345"
    }
    res = client.post("/students/", json=student_data)
    new_student = StudentOut(**res.json())
    
    assert res.status_code == 201
    
    return new_student