from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Construction_and_Extraction_instances import create_construction_and_extraction_instances
from models import engine, Construction_and_Extraction


with Session(engine) as session:
    instances = create_construction_and_extraction_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
