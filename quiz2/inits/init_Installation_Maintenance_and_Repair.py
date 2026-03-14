from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Installation_Maintenance_and_Repair_instances import create_installation_maintenance_and_repair_instances
from models import engine, Installation_Maintenance_and_Repair


with Session(engine) as session:
    instances = create_installation_maintenance_and_repair_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
