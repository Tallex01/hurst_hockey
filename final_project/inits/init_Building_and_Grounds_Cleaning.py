from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Building_and_Grounds_Cleaning_instances import create_building_and_grounds_cleaning_instances
from models import engine, Building_and_Grounds_Cleaning


with Session(engine) as session:
    instances = create_building_and_grounds_cleaning_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
