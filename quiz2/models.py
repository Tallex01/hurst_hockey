from sqlmodel import SQLModel, Field, create_engine

class Groups(SQLModel, table=True):
    job_group: str = Field(default=None, primary_key=True)
    annual_openings: int | None = None
    med_annual_pay: int | None = None

class Architecture_and_Engineering(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Arts_and_Design(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Building_and_Grounds_Cleaning(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Business_and_Financial(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Community_and_Social_Service(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Computer_and_Information_Technology(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Construction_and_Extraction(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Educational_Instruction_and_Library(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Entertainment_and_Sports(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Farming_Fishing_and_Forestry(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Food_Preparation_and_Serving(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Healthcare(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Installation_Maintenance_and_Repair(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Legal(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Life_Physical_and_Social_Science(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Management(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Math(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Media_and_Communication(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Office_and_Administrative_Support(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Personal_Care_and_Service(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Production(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Protective_Service(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Sales(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

class Transportation_and_Material_Moving(SQLModel, table=True):
    job_name: str = Field(default=None, primary_key=True)
    job_group: str = Field(default=None, foreign_key="groups.job_group")
    annual_openings: int | None = None
    med_annual_pay: int | None = None
    entry_lvl_ed: str | None = None

engine = create_engine("sqlite:///bls.db")
SQLModel.metadata.create_all(engine)

#If a job entry level education says "See how to become one", put NA
#need to rerun populating them with this caveat