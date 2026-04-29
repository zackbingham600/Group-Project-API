from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User

router = APIRouter()


# GET ALL USERS
@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# SAVE / UPDATE USER
@router.post("/save")
def save_user(data: dict, db: Session = Depends(get_db)):

    username = data.get("username", "You")

    user = db.query(User).filter(User.username == username).first()

    if not user:
        user = User(
            username=username,
            email=data.get("email", "user@email.com"),
            role="staff"
        )
        db.add(user)

    user.steps = data.get("steps", 0)
    user.mood = data.get("mood", 0)
    user.points = data.get("points", 0)
    user.challenges_completed = data.get("challenges_completed", 0)

    db.commit()
    db.refresh(user)

    return {
        "message": "User saved successfully",
        "user": user.username
    }