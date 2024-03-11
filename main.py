from fastapi import FastAPI
from typing import Optional

app = FastAPI()

items = {
    1: {"name": "Honda", "price": 10.99},
    2: {"name": "Yamaha", "price": 9.99},
    3: {"name": "Kawasaki", "price": 12.99},
}

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to My API Server on Cloud Run - CI/CD"}

@app.get("/items/{item_id}")
async def get_data(item_id: int):
    return {"message": "Data retrieve successfully!"}

@app.put("/items/{item_id}")
async def update_data(item_id: int, data: dict):
    print(item_id)
    return {"message": "Data updated successfully!"}

@app.post("/add")
async def create_data(data: dict):
    print(data)
    return {"message": "Data created successfully!"}

@app.delete("/items/{item_id}")
async def delete_data(item_id: int, data: dict):
    print(data)
    return {"message": "Data deleted successfully!"}

@app.patch("/items/{item_id}")
async def patch_data(item_id: int, data: dict):
    print(item_id, data)
    return {"message": "Data patched successfully!"}