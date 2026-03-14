from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Transportation_and_Material_Moving_instances import create_transportation_and_material_moving_instances
from models import engine, Transportation_and_Material_Moving


with Session(engine) as session:
    instances = create_transportation_and_material_moving_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
