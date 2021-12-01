# Tarea Operaciones Matematicas
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# uvicorn (nombre del archivo):app --reload

# Crear clases
class Item(BaseModel):
    a: int = None
    b: int = None

# Funcion para Sumar
@app.get("/Suma")
def Suma(a: int, b: int):
    c = a + b
    result = {'a': a, 'b': b, 'a+b': c}
    return result

# Funcion para Sumar
@app.post("/Suma")
def Suma(a: int, b: int):
    c = a + b
    result = {'a': a, 'b': b, 'a+b': c}
    return result


# Funcion para Restar
@app.get("/Resta")
def Resta(a: int, b: int):
    c = a - b
    result = {'a': a, 'b': b, 'a-b': c}
    return result

# Funcion para Restar
@app.post("/Resta")
def Resta(a: int, b: int):
    c = a - b
    result = {'a': a, 'b': b, 'a-b': c}
    return result


# Funcion para Multiplicar
@app.get("/Multiplicacion")
def Multiplicacion(a: int, b: int):
    c = a * b
    result = {'a': a, 'b': b, 'a*b': c}
    return result

# Funcion para Multiplicar
@app.post("/Multiplicacion")
def Multiplicacion(a: int, b: int):
    c = a * b
    result = {'a': a, 'b': b, 'a*b': c}
    return result


# Funcion para Dividir
@app.get("/Division")
def Division(a: int, b: int):
    c = a / b
    result = {'a': a, 'b': b, 'a/b': c}
    return result

# Funcion para Dividir
@app.post("/Division")
def Division(a: int, b: int):
    c = a / b
    result = {'a': a, 'b': b, 'a/b': c}
    return result


































