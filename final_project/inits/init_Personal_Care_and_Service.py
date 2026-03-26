from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Personal_Care_and_Service_instances import create_personal_care_and_service_instances
from models import engine, Personal_Care_and_Service


with Session(engine) as session:
    instances = create_personal_care_and_service_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
