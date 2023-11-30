from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["root"])
async def root():
    return {"message": "If you see this, the Github trigger cloud build work. at even at home Mac Mini. also work!!!"}