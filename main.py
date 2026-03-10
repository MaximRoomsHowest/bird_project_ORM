from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import start_db  # your database setup
from routers.species import router as species_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    start_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "API is running"}

app.include_router(species_router)