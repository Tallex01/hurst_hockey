from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException
from models import Groups, engine
from sqlalchemy import func, select as sa_select
from sqlmodel import SQLModel
from sqlmodel import Session, select
import re

app = FastAPI()


@app.get("/groups")
def list_groups():
	with Session(engine) as session:
		statement = select(Groups).order_by(Groups.job_group)
		groups = session.exec(statement).all()
		return groups


@app.get("/group/{job_group}")
def get_group(job_group: str):
	with Session(engine) as session:
		statement = select(Groups).where(Groups.job_group == job_group)
		group = session.exec(statement).first()

		if group is None:
			raise HTTPException(status_code=404, detail="Job group not found")

		return group


def _normalize_group_name(name: str) -> str:
	cleaned = re.sub(r"[^a-z0-9]+", "_", name.lower())
	return re.sub(r"_+", "_", cleaned).strip("_")


def _job_tables():
	return [
		table
		for table in SQLModel.metadata.tables.values()
		if table.name != "groups" and "job_name" in table.c
	]


@app.get("/group/{job_group}/jobs")
def get_jobs_for_group(job_group: str):
	with Session(engine) as session:
		group_statement = select(Groups).where(Groups.job_group == job_group)
		group = session.exec(group_statement).first()

		if group is None:
			raise HTTPException(status_code=404, detail="Job group not found")

		normalized_group = _normalize_group_name(job_group)						# remove occupations suffix and normalize to match table names
		candidate_table_names = [normalized_group]
		if normalized_group.endswith("_occupations"):
			candidate_table_names.append(normalized_group.removesuffix("_occupations"))

		table = None													#accessing the table
		for candidate in candidate_table_names:
			table = SQLModel.metadata.tables.get(candidate)
			if table is not None:
				break

		if table is None:
			raise HTTPException(
				status_code=404,
				detail=f"No jobs table found for group '{job_group}'",
			)

		job_rows = session.execute(sa_select(table)).mappings().all()
		return [dict(row) for row in job_rows]


@app.get("/job/{job_name}")
def get_job(job_name: str):
	with Session(engine) as session:
		for table in _job_tables():
			statement = sa_select(table).where(func.lower(table.c.job_name) == job_name.lower())
			job_row = session.execute(statement).mappings().first()
			if job_row is not None:
				return dict(job_row)

		raise HTTPException(status_code=404, detail="Job not found")





app.mount("/", StaticFiles(directory="static", html=True), name="static")