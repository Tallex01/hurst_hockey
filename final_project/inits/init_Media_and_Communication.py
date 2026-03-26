from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Media_and_Communication_instances import create_media_and_communication_instances
from models import engine, Media_and_Communication


with Session(engine) as session:
    instances = create_media_and_communication_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
