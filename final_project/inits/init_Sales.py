from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Sales_instances import create_sales_instances
from models import engine, Sales


with Session(engine) as session:
    instances = create_sales_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
