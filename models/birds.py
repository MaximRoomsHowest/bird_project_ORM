from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel
from models.species import Species
from models.birdspotting import BirdSpotting


class BirdBase(SQLModel):
    nickname: str
    ring_code: str
    age: int


class Bird(BirdBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    species_id: int = Field(foreign_key="species.id")
    species: Optional[Species] = Relationship()

    spottings: List[BirdSpotting] = Relationship(back_populates="bird")


class BirdCreate(BirdBase):
    species_id: int