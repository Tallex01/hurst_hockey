from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Entertainment_and_Sports_instances import create_entertainment_and_sports_instances
from models import engine, Entertainment_and_Sports


with Session(engine) as session:
    instances = create_entertainment_and_sports_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
