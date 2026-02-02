# Employee request and response schemas
# Validates employee API input/output

from pydantic import BaseModel, EmailStr
from uuid import UUID


class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str


class EmployeeResponse(BaseModel):
    id: UUID
    employee_id: str
    full_name: str
    email: str
    department: str

    class Config:
        from_attributes = True

