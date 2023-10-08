#Python
from typing import Optional

#pPydantic
from pydantic import BaseModel

#Fastapi
from fastapi import FastAPI
from fastapi import Body, Query, Path

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
    name: Optional[str] = Query(
        None,
        min_Length=1, 
        max_Length=50,
        title="Person Name",
        description="this is the person name. It's between 1 an 50 characters"
        ),
    age: int = Query(
        ...,
        title = "Person Age",
        description="This is the person age. It's required")
):
    return {name: age}

# Validaciones: Path Parameters    

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0
        )
):
    return {person_id: "It exists"}