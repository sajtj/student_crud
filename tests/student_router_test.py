from student.schemas import StudentOut

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

def test_create_student(client):
    res = client.post("/students/", json=student_data)
    new_student = StudentOut(**res.json())
    
    assert new_student.id == 1
    assert new_student.name == "Sajad"
    assert res.status_code == 201

def test_read_students(client, test_student):
    res = client.get("/students/")
    assert len(res.json()) == 1
    assert res.status_code == 200
    
def test_read_student(client, test_student):
    res = client.get("/students/1/")
    student = StudentOut(**res.json())
    assert student.name == "Sajad"
    assert res.status_code == 200
    
def test_update_student(client, test_student):
    updated_student_data = student_data
    updated_student_data["name"] = "Ali"
    res = client.put("/students/1/", json=updated_student_data)
    student = StudentOut(**res.json())
    assert student.name == "Ali"
    assert student.last_name == "Tajik"
    assert res.status_code == 200
    
def test_delete_student(client, test_student):
    res = client.delete("/students/1/")
    assert res.status_code == 204