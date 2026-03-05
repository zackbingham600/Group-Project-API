from sqlalchemy.orm import Session
from models import test_model
from schema.test_schema import testModelRequest

class TestRepository:

    def get_all(self, db: Session):
        return db.query(test_model.Test).all()

    def insert_test_message(self, db: Session, message: testModelRequest):
        #Generates the dictionary version of the message model
        db_test = test_model.Test(**message.model_dump())
        #inserts record into table
        db.add(db_test)
        #Commits to the database
        db.commit()
        #refresh the data
        db.refresh(db_test)
        # return record added
        return db_test
