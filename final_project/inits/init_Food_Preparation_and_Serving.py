from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Food_Preparation_and_Serving_instances import create_food_preparation_and_serving_instances
from models import engine, Food_Preparation_and_Serving


with Session(engine) as session:
    instances = create_food_preparation_and_serving_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
