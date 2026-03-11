from sqlmodel import Session, select
from models.birds import Bird, BirdCreate
from models.species import Species

class BirdRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Bird)
        return self.session.exec(statement).all()

    def insert(self, payload: BirdCreate):
        # Check that the species exists
        species = self.session.get(Species, payload.species_id)
        if not species:
            raise ValueError(f"Species with id {payload.species_id} does not exist")

        bird = Bird(**payload.dict())
        self.session.add(bird)
        self.session.commit()
        self.session.refresh(bird)
        return bird