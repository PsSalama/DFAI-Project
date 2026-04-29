from fastapi import FastAPI
from fastapi import Query, Path, Body
from src.dataHandling.app.services.process import *
from src.dataHandling.app.services.registry import *
from src.dataHandling.app.dtos.User import *

app = FastAPI()
MEM_PATH = r"C:\Users\Admin\Downloads\memdump_4.mem"

@app.get("/process")
def process_endpoint():
    return process(MEM_PATH, "list_process.txt")

@app.get("/registry")
def registry_endpoint(user_id):
    return registry(MEM_PATH, "list_registry.txt")

@app.get("/user/{user_id}")
def registry_endpoint(user_id : int):
    return {"user_id": user_id}

@app.get("/query")
def registry_endpoint(name:str, age:int):
    return {"user_name": name, "age": age}

@app.post("/register")
def register_endpoint(user_register_data: register_data):
    return user_register_data.email

@app.put("/user/{user_id}")
def update_endpoint(user_id: int, user_register_data: register_data):
    return {"user_id": user_id, **user_register_data.model_dump()}

@app.get("/validate")
def validate_endpoint(name:str = Query(..., min_length=3, max_length=7, regex="^[a-z]+$")):
    return {"name": name}

@app.get("/item/{item_id}")
def user_endpoint(item_id:int = Path(..., ge=1)):
    return {"item_id": item_id}

@app.post("/item")
def create_item_endpoint(number:int = Body(...)):
    return {"item_number": number}
