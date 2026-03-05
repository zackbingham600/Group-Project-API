from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:8000"],
    allow_methods=["*"],
    allow_headers=["*"],   
    allow_credentials=True
)
@app.get("/test")
def test_endpoint():
    return {"message": "Hello from FastAPI!", "status": "success"}