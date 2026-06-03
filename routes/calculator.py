from fastapi import APIRouter
from models.numbers import Numbers
from services.calculator_service import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
)

router = APIRouter(
    prefix="/calculator",
    tags=["Calculator"]
)

@router.get("/add")
def add(a: float, b:float):
    return{"result": add_numbers(a,b)}

@router.get("/subtract")
def subtract(a: float, b:float):
    return{"result": subtract_numbers(a,b)}

@router.post("/multiply")
def multiply(numbers: Numbers):
    return{"result": multiply_numbers(numbers.a, numbers.b)}