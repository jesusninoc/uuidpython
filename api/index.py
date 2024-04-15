import uuid
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
async def generar_uuid():
    return {"uuid": str(uuid.uuid4())}

