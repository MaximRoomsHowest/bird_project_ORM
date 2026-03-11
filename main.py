from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import start_db
from routers.species import router as species_router
from routers.birds import router as birds_router
from routers.birdspotting import router as birdspotting_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "API is running"}

app.include_router(species_router)
app.include_router(birds_router)
app.include_router(birdspotting_router)