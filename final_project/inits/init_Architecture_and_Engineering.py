from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Architecture_and_Engineering_instances import create_architecture_and_engineering_instances
from models import engine, Architecture_and_Engineering


with Session(engine) as session:
    instances = create_architecture_and_engineering_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
