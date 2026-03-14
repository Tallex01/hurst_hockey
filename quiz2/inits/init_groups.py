from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from group_instances import create_group_instances
from models import engine, Groups


with Session(engine) as session:
    instances = create_group_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
