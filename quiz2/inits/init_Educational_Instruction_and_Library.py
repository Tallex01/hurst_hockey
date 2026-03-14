from pathlib import Path
import sys
from sqlmodel import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from instances.Educational_Instruction_and_Library_instances import create_educational_instruction_and_library_instances
from models import engine, Educational_Instruction_and_Library


with Session(engine) as session:
    instances = create_educational_instruction_and_library_instances()
    for instance in instances:
        session.merge(instance)
    session.commit()
