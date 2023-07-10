from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# GET - get information
# POST - create something new
# PUT - Update an object
# DELETE - Delete something

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": 2019
    },
    2: {
        "name": "john",
        "age": 17,
        "year": 2018
    }
}

class CreateStudent(BaseModel):
    name: str
    age: int
    year: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view"), gt=0, lt=3):
    return students[student_id]

@app.get("/get-by-name/")
def get_student(name: Optional[str] = None):
    students_by_name = []
    for student_id in students:
        if students[student_id]["name"] == name:
            students_by_name.append(students[student_id])
    return students_by_name

    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: CreateStudent):

    if student_id in students:
        return{"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):

    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

