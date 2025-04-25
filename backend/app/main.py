from fastapi import FastAPI
from .routes.actors import router as actor_router

app = FastAPI()
app.include_router(actor_router)

@app.get("/")
def root():
    return {"message": "Hello World"}