from pydantic import BaseModel

class Student(BaseModel):
    id:int
    name:str
    department:str
    marks:float
    email:str

class TextData(BaseModel):
    text:str

class Calculation(BaseModel):
    number1:float
    number2:float
    operation:str

class PromptData(BaseModel):
    prompt:str