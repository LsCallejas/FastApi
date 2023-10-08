#Python
from typing import Optional

#pPydantic
from pydantic import BaseModel

#Fastapi
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

#Models

class Person(BaseModel): 
    first_name: str
    last_name: str
    age: int
    hait_colo: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
def home():
    return {"hello": "world"}

# Request and Resoinse Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

# Validaciones: Query Parameters  

@app.get("/person/detail")
def Show_person(
    name: Optional[str] = Query(None, min_Length=1, max_Length=50),
    age: int = Query(...)
):
    return {name: age}