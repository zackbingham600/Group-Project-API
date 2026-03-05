from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/testing", tags=["tests"])

@router.get("/test")
def test_endpoint():
    return {"message": "Hello from FastAPI!", "status": "success"}
