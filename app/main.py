# Entry point of HRMS Lite backend
# Initializes app, database tables and API routes

from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import employee, attendance
from app.routes.employee import router as employee_router
from app.routes.attendance import router as attendance_router

FRONTEND_URL = os.getenv("FRONTEND_URL")

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        FRONTEND_URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_router)
app.include_router(attendance_router)

@app.get("/")
def root():
    return {"message": "HRMS Lite backend running"}
