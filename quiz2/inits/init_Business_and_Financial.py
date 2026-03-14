from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Business_and_Financial_instances import create_business_and_financial_instances
from models import engine, Business_and_Financial


with Session(engine) as session:
    instances = create_business_and_financial_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
