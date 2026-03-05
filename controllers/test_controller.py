from fastapi import APIRouter, Depends, HTTPException
from schema.test_schema import testModelRequest, testResponse
from services.test_service import TestService
from sqlalchemy.orm import Session

from database.db import get_db

router = APIRouter(prefix="/testing", tags=["tests"])
service = TestService()


@router.get("/test")
def test_endpoint():
    return {"message": "Hello from FastAPI!", "status": "success"}


@router.post("/insertTestMessage", response_model=testResponse)
def insert_test_endpoint(test_message: testModelRequest, db: Session = Depends(get_db)):
    response = service.create_user(db, test_message)
    return {response}
