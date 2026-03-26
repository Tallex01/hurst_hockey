from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Computer_and_Information_Technology_instances import create_computer_and_information_technology_instances
from models import engine, Computer_and_Information_Technology


with Session(engine) as session:
    instances = create_computer_and_information_technology_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
