from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()

@router.get("/{item_id}", response_description="Retrieve a record")
async def get_data(item_id: int):
    return {"message": "Data retrieve successfully!"}

@router.put("/{item_id}", response_description="Update a record")
async def update_data(item_id: int, data: dict):
    print(item_id)
    return {"message": "Data updated successfully!"}

@router.post("/{item_id}", response_description="Create a new record")
async def create_data(item_id: int, data: dict):
    print(data)
    return {"message": "Data created successfully!"}

@router.delete("/{item_id}", response_description="Delete a record")
async def delete_data(item_id: int, data: dict):
    print(data)
    return {"message": "Data deleted successfully!"}

@router.patch("/{item_id}", response_description="Modify data in a record")
async def patch_data(item_id: int, data: dict):
    print(item_id, data)
    return {"message": "Data patched successfully!"}