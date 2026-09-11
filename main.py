from fastapi import FastAPI,HTTPException
from models import Student,TextData,Calculation,PromptData
from services import calculate_result,analyze_text,generate_response

app=FastAPI(title="Mini AI Backend")

students=[
    {"id":1,"name":"Praneeth","department":"IT","marks":90,"email":"praneeth1896@gmail.com"},
    {"id":2,"name":"Virat","department":"CSE","marks":95,"email":"virat18@gmail.com"}
]

@app.get("/health")
def health():
    return {"status":"healthy","message":"API is running"}

@app.get("/students")
def get_students():
    return students

@app.post("/students",status_code=201)
def add_student(student:Student):
    for existing in students:
        if existing["id"]==student.id:
            raise HTTPException(status_code=400,detail="Student ID already exists")
    students.append(student.model_dump())
    return {"message":"Student added successfully","student":student}

@app.get("/students/{id}")
def get_student(id:int):
    for student in students:
        if student["id"]==id:
            return student
    raise HTTPException(status_code=404,detail="Student not found")

@app.post("/analyze-text")
def analyze_text_api(data:TextData):
    return analyze_text(data.text)

@app.post("/calculate")
def calculate(data:Calculation):
    try:
        result=calculate_result(data.number1,data.number2,data.operation)
        return {"result":result}
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@app.post("/generate")
def generate(data:PromptData):
    return {
        "prompt":data.prompt,
        "response":generate_response(data.prompt)
    }
