# Entry point of backend app
# Creates FastAPI instance and root test route
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.database import engine, Base
from app.models import employee, attendance

Base.metadata.create_all(bind=engine)
app = FastAPI(title="HRMS Lite API")

@app.get("/")
def root():
    return {"message": "HRMS Lite backend running"}
