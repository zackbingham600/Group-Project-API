from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/testing", tags=["fitness"])

# 🧠 TEMP STORAGE (works immediately, no DB needed)
data_store = {
    "steps": 0,
    "mood": 0,
    "points": 0
}

# 📦 Request model
class FitnessData(BaseModel):
    steps: int
    mood: int
    points: int


# ✅ GET → fetch data
@router.get("/test")
def get_data():
    return data_store


# ✅ POST → save data
@router.post("/test")
def save_data(data: FitnessData):
    data_store["steps"] = data.steps
    data_store["mood"] = data.mood
    data_store["points"] = data.points

    return {
        "message": "Saved successfully",
        "data": data_store
    }