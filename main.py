from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["root"])
async def root():
    return {"message": "If you see this, the Github trigger cloud build work"}