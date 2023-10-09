#Python
from typing import Optional
from enum import Enum

#pPydantic
from pydantic import BaseModel
from pydantic import Field 

#Fastapi
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

#Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blode = "blode"
    red = "red"


class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel): 
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hait_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

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

#Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person: Person = Body(...),
    Location: Location = Body(...)
):
    results = person.dict()
    results.update(Location.dict())
    return person