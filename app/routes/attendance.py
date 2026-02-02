# Attendance API routes
# Handles mark and view attendance records

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from uuid import UUID

from app.models.attendance import Attendance
from app.models.employee import Employee
from app.schemas.attendance import AttendanceCreate, AttendanceResponse
from app.core.deps import get_db

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post(
    "/",
    response_model=AttendanceResponse,
    status_code=status.HTTP_201_CREATED
)
def mark_attendance(
    payload: AttendanceCreate,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(
        Employee.id == payload.employee_id
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    if payload.status not in ["PRESENT", "ABSENT"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be PRESENT or ABSENT"
        )

    attendance = Attendance(
        employee_id=payload.employee_id,
        date=payload.date,
        status=payload.status
    )

    try:
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this date"
        )

    return attendance


@router.get(
    "/",
    response_model=list[AttendanceResponse]
)
def get_attendance(
    employee_id: UUID,
    db: Session = Depends(get_db)
):
    return (
        db.query(Attendance)
        .filter(Attendance.employee_id == employee_id)
        .all()
    )
