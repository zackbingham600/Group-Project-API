from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import test_controller
from database.db import engine, Base

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:8000"],
    allow_methods=["*"],
    allow_headers=["*"],   
    allow_credentials=True
)

Base.metadata.create_all(bind=engine)
app.include_router(test_controller.router)