from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Protective_Service_instances import create_protective_service_instances
from models import engine, Protective_Service


with Session(engine) as session:
    instances = create_protective_service_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
