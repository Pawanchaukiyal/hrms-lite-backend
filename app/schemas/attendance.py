# Attendance request and response schemas
# Ensures valid attendance data

from pydantic import BaseModel
from datetime import date

class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: str

class AttendanceResponse(BaseModel):
    id: str
    employee_id: str
    date: date
    status: str

    class Config:
        orm_mode = True
