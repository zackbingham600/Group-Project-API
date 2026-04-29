from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "sqlite:///./fitness.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Fitness(Base):
    __tablename__ = "fitness"

    id = Column(Integer, primary_key=True, index=True)
    steps = Column(Integer, default=0)
    mood = Column(Integer, default=0)
    points = Column(Integer, default=0)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/test")
def get_data(db: Session = Depends(get_db)):
    data = db.query(Fitness).first()

    if not data:
        data = Fitness(steps=0, mood=0, points=0)
        db.add(data)
        db.commit()
        db.refresh(data)

    return {
        "steps": data.steps,
        "mood": data.mood,
        "points": data.points
    }

@app.post("/test")
def save_data(new_data: dict, db: Session = Depends(get_db)):
    data = db.query(Fitness).first()

    if not data:
        data = Fitness()

    data.steps = new_data.get("steps", 0)
    data.mood = new_data.get("mood", 0)
    data.points = new_data.get("points", 0)

    db.add(data)
    db.commit()

    return {"message": "Saved"}