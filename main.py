from fastapi import FastAPI
from pydantic import BaseModel
from models.numbers import Numbers
from routes.calculator import router as calculator_router

class CalculationResult(BaseModel):
    result: float
    operation: str

app = FastAPI()
app.include_router(calculator_router)

@app.get("/")
def root():
    return{"message": "Hello from FastAPI"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
