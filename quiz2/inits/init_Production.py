from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Production_instances import create_production_instances
from models import engine, Production


with Session(engine) as session:
    instances = create_production_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
