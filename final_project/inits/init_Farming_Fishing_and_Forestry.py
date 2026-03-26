from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Farming_Fishing_and_Forestry_instances import create_farming_fishing_and_forestry_instances
from models import engine, Farming_Fishing_and_Forestry


with Session(engine) as session:
    instances = create_farming_fishing_and_forestry_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
