from sqlmodel import Session, select
from models.birdspotting import BirdSpotting, BirdSpottingCreate
from models.birds import Bird


class BirdSpottingRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(BirdSpotting)
        return self.session.exec(statement).all()

    def get_one(self, spotting_id: int):
        return self.session.get(BirdSpotting, spotting_id)

    def insert(self, payload: BirdSpottingCreate):

        bird = self.session.get(Bird, payload.bird_id)
        if not bird:
            raise ValueError("Bird does not exist")

        spotting = BirdSpotting(**payload.dict())

        self.session.add(spotting)
        self.session.commit()
        self.session.refresh(spotting)

        return spotting