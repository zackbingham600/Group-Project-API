from fastapi import APIRouter
from sqlalchemy.orm import Session
from repositories.test_repo import TestRepository
from schema.test_schema import testModelRequest

class TestService:
    def __init__(self):
        self.repo = TestRepository()

    def create_user(self, db: Session, test: testModelRequest):

        return self.repo.insert_test_message(db, test)

    def get_users(self, db: Session):

        return self.repo.get_all(db)