from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException
from models import Groups, engine
from sqlmodel import Session, select

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







app.mount("/", StaticFiles(directory="static", html=True), name="static")