from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Math_instances import create_math_instances
from models import engine, Math


with Session(engine) as session:
    instances = create_math_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
