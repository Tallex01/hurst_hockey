from sqlmodel import Session
from bio_instances import create_bio_instances
from models import engine, Bio

with Session(engine) as session:
    bio_instances = create_bio_instances()
    session.add_all(bio_instances)
    session.commit()

