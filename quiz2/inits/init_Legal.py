from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Legal_instances import create_legal_instances
from models import engine, Legal


with Session(engine) as session:
    instances = create_legal_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
