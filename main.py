# Librerias
import io
from enum import Enum
import pandas as pd

from fastapi import FastAPI
from typing import Dict, Optional
from pydantic import BaseModel
from fastapi.responses import UJSONResponse, HTMLResponse, StreamingResponse


# se inicia fastapi y con ello la aplicacion
app = FastAPI()

#crear clase, para validar los roles. Son Numeradores
class RoleName(str, Enum):
    admin = "Admin"
    writer = "Writer"
    reader = "Reader"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float]


# decorador: referencia a la aplicacion.
# definir Rutas @app
@app.get("/")
def root():
    return {"message": "Hello Margerys, Galileo Master!!! Section V"}


# obtener parametros (URL, Headers, Body), corresponden al PATH
# cada vez que se defina un funcion, trata de ser clara las instrucciones
# Nota: esta ruta se actualizo en la parte de abajo
#@app.get("/items/{item_id}")
#def read_item(item_id: int) -> Dict[str, int]:
#    return {"item_id": item_id}


# el orden en las funciones es muy importante, porque FastAPI va agregando las rutas a sus listas
# ejem: definir una ruta que no tenga parametros
@app.get("/users/me")
def read_current_user():
    return {"user_id": "The currrent logged user."}


# funciones user_id
@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


# definicion de roles (adminstrador:full permiso, escritor:leer y escribir, lector:leer)
@app.get("/roles/{role_name}")
def get_role_permissions(role_name: RoleName):
    if role_name == RoleName.admin:
        return {"role_name": role_name, "permissions": "Full access"}

    if role_name == RoleName.writer:
        return {"role_name": role_name, "permissions": "write access"}

    return {'role_name': role_name, "permissions": "Read access only"}


# Parametros de Query
fake_items_db = [{"item_name": "uno"}, {"item_name": "dos"}, {"item_name": "tres"}]

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip+limit]

@app.get("/items/{item_id")
def read_item(item_id: int, query: Optional[str] = None):
    message = {"item_id": item_id}
    if query:
        message['query'] = query

    return message


# Ejemplo
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: int, query: Optional[str] = None, describe: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}

    if query:
        item['query'] = query

    if describe:
        item['description'] = "This is a log description for the item"

    return item


# POST
# las rutas se pueden reutilizar siempre que los verbos sean diferentes,
# no pueden existir dos rutas con el mismo verbo
@app.post("/item/")
def create_item(item: Item):
    return {
        "message": "This item was successfully created",
        "item": item.dict()
    }

# Actualizacion de servicios
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item.tax == 0 or item.tax is None:
        item.tax = item.price * 0.12

    return {
        "message": "the item was update",
        "item_id": item_id,
        "item": item.dict()
    }


# Tipo de respuestas
@app.get("/itemsall", response_class=UJSONResponse)
def read_long_json():
    return [{"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"},
            {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"},
            {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"},
            {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}, {"item_id": "item"}]

@app.get("/html/", response_class=HTMLResponse)
def read_html():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

# definir funcion que nos devuelva en CSV
@app.get("/csv")
def get_csv():

    df = pd.DataFrame({"Column A": [1,2], "Column B": [3,4]})

    stream = io.StringIO()

    df.to_csv(stream, index=False)

    response = StreamingResponse(iter([stream.getvalue()]), media_type='text/csv')

    response.headers['Content-Disposition'] = "attachment; filename=my_awesome_report.csv"

    return response
































