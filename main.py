from fastapi import FastAPI
from pydantic import BaseModel

class CalculationResult(BaseModel):
    result: float
    operation: str

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Hello from FastAPI"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/calculator")
def calculator(a: int, b: int):
    return {
        "result": a + b
    }

@app.get("/add", response_model=CalculationResult)
def add(a: int, b: int):
    return {"result": a + b, "operation": "addition"}

@app.get("/subtract")
def subtract(a: int, b:int):
    return {"result": a - b}
