import uuid
from fastapi import FastAPI

app = FastAPI()

@app.post("/api/")
async def generar_uuid():
    return {"uuid": str(uuid.uuid4())}

