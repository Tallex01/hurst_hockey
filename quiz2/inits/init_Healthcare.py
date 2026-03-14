from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Healthcare_instances import create_healthcare_instances
from models import engine, Healthcare


with Session(engine) as session:
    instances = create_healthcare_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
