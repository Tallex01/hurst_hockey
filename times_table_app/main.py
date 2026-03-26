from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

#1st endpoint
@app.get("/numbers")
async def get_number():
    n1 = random.randint(0,12)
    n2 = random.randint(0,12)
    return {"n1": n1, "n2": n2}

#2nd endpoint
@app.get("/multiply")
async def mult(n1: int, n2: int):
    return{"product": n1*n2}
   


app.mount("/", StaticFiles(directory="static", html=True), name="static")

#kill -9 $(lsof -ti:8000) 2>/dev/null || true

