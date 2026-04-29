from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import User

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/save")
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

    return {"message": "User saved successfully", "user": user.username}

