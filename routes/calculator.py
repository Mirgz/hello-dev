from fastapi import APIRouter
from models.numbers import Numbers

router = APIRouter(
    prefix="/calculator",
    tags=["Calculator"]
)

@router.get("/add")
def add(a: float, b:float):
    return{"result": a + b}

@router.get("/subtract")
def subtract(a: float, b:float):
    return{"result": a - b}

@router.post("/multiply")
def multiply(numbers: Numbers):
    return{"result": numbers.a * numbers.b}