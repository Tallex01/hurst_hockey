from sqlmodel import SQLModel, Field, create_engine

class Groups(SQLModel, table=True):
    job_group: str = Field(default=None, primary_key=True)
    annual_openings: int | None = None
    med_annual_pay: int | None = None

class Architecture(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="Groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

engine = create_engine("sqlite:///jobs.db")
SQLModel.metadata.create_all(engine)