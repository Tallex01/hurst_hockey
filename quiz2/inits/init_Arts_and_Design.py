from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Arts_and_Design_instances import create_arts_and_design_instances
from models import engine, Arts_and_Design


with Session(engine) as session:
    instances = create_arts_and_design_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
