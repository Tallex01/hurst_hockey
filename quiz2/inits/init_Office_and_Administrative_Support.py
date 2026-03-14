from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Office_and_Administrative_Support_instances import create_office_and_administrative_support_instances
from models import engine, Office_and_Administrative_Support


with Session(engine) as session:
    instances = create_office_and_administrative_support_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
