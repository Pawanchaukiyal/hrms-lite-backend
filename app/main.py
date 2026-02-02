# Entry point of HRMS Lite backend
# Initializes app, database tables and API routes

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.database import Base, engine
from app.models import employee, attendance
from app.routes.employee import router as employee_router
from app.routes.attendance import router as attendance_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

app.include_router(employee_router)
app.include_router(attendance_router)


@app.get("/")
def root():
    return {"message": "HRMS Lite backend running"}
