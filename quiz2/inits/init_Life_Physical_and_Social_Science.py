from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Life_Physical_and_Social_Science_instances import create_life_physical_and_social_science_instances
from models import engine, Life_Physical_and_Social_Science


with Session(engine) as session:
    instances = create_life_physical_and_social_science_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
