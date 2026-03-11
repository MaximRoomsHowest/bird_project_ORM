from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from database import get_session
from repositories.birdspotting import BirdSpottingRepository
from models.birdspotting import BirdSpotting, BirdSpottingCreate

router = APIRouter(prefix="/birdspotting", tags=["Birdspotting"])


def get_repo(
    session: Annotated[Session, Depends(get_session)]
) -> BirdSpottingRepository:
    return BirdSpottingRepository(session)


@router.get("/", response_model=List[BirdSpotting])
async def get_all(repo: Annotated[BirdSpottingRepository, Depends(get_repo)]):
    return repo.get_all()


@router.get("/{spotting_id}", response_model=BirdSpotting)
async def get_one(
    spotting_id: int,
    repo: Annotated[BirdSpottingRepository, Depends(get_repo)]
):
    spotting = repo.get_one(spotting_id)

    if not spotting:
        raise HTTPException(status_code=404, detail="Spotting not found")

    return spotting


@router.post("/", response_model=BirdSpotting)
async def create(
    spotting: BirdSpottingCreate,
    repo: Annotated[BirdSpottingRepository, Depends(get_repo)]
):
    try:
        return repo.insert(spotting)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )