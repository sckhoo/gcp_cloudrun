from fastapi import FastAPI
from typing import Optional
from routes import router as items_router


app = FastAPI()

items = {
    1: {"name": "Honda", "price": 10.99},
    2: {"name": "Yamaha", "price": 9.99},
    3: {"name": "Kawasaki", "price": 12.99},
}

@app.on_event("startup")
def startup_db_client():
    # app.mongodb_client = MongoClient(config["ATLAS_URI"])
    # app.database = app.mongodb_client[config["DB_NAME"]]
    print("connecting to DB, send message to log")
    
@app.on_event("shutdown")
def shutdown_db_client():
    # app.mongodb_client.close()
    print("closing db connection, send message to log")

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to My API Server on Cloud Run - Cloud Mile CI/CD Demo v2"}

app.include_router(items_router, tags=["items"], prefix="/items")