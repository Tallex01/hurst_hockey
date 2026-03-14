from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Community_and_Social_Service_instances import create_community_and_social_service_instances
from models import engine, Community_and_Social_Service


with Session(engine) as session:
    instances = create_community_and_social_service_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
