# Attendance request and response schemas
# Validates attendance data (UUID-safe, Pydantic v2)

from pydantic import BaseModel
from uuid import UUID
from datetime import date


class AttendanceCreate(BaseModel):
    employee_id: UUID
    date: date
    status: str


class AttendanceResponse(BaseModel):
    id: UUID
    employee_id: UUID
    date: date
    status: str

    class Config:
        from_attributes = True
