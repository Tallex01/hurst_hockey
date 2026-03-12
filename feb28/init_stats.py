from sqlmodel import Session
from feb28.stats_instances import create_stats_instances
from models import engine, Stats

with Session(engine) as session:
    stats_instances = create_stats_instances()
    session.add_all(stats_instances)
    session.commit()

