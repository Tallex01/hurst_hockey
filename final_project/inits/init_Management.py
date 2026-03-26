from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Management_instances import create_management_instances
from models import engine, Management


with Session(engine) as session:
    instances = create_management_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
