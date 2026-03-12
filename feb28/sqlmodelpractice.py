from sqlmodel import Session, select
from bio_instances import create_bio_instances
from models import engine, Bio

with Session(engine) as session:
    statement = select(Bio).where(Bio.last_name.like("S%"))
    results = session.exec(statement)
    for bio in results:
        print(bio)


#1 Select all rows in bio
# from sqlmodel import Session, select
# from bio_instances import create_bio_instances
# from models import engine, Bio

# with Session(engine) as session:
#     statement = select(Bio)
#     results = session.exec(statement)
#     for bio in results:
#         print(bio)

#2 Select first_name and last_name and position for all rows in bio
# from sqlmodel import Session, select
# from bio_instances import create_bio_instances
# from models import engine, Bio

# with Session(engine) as session:
#     statement = select(Bio.first_name, Bio.last_name, Bio.position)
#     results = session.exec(statement)
#     for bio in results:
#         print(bio)

#3 Find players with weight >200
# from sqlmodel import Session, select
# from bio_instances import create_bio_instances
# from models import engine, Bio

# with Session(engine) as session:
#     statement = select(Bio).where(Bio.weight > 200)
#     results = session.exec(statement)
#     for bio in results:
#         print(bio)

#4 find players where position = "Goaltender" and weight > 190
# from sqlmodel import Session, select
# from bio_instances import create_bio_instances
# from models import engine, Bio

# with Session(engine) as session:
#     statement = select(Bio).where((Bio.weight > 190) & (Bio.position == "Goaltender"))
#     results = session.exec(statement)
#     for bio in results:
#         print(bio)

#5 Find players where position == "Goaltender" OR weight > 210
# from sqlmodel import Session, select
# from bio_instances import create_bio_instances
# from models import engine, Bio

# with Session(engine) as session:
#     statement = select(Bio).where((Bio.weight > 210) | (Bio.position == "Goaltender"))
#     results = session.exec(statement)
#     for bio in results:
#         print(bio)

#6 Find players whose last_name starts with "S"
from sqlmodel import Session, select
from bio_instances import create_bio_instances
from models import engine, Bio

with Session(engine) as session:
    statement = select(Bio).where(Bio.last_name.like("S%"))
    results = session.exec(statement)
    for bio in results:
        print(bio)


