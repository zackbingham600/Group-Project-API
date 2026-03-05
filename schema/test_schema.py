from pydantic import BaseModel


class testResponse(BaseModel):
    message: str

    class Config:
        from_attributes = True

class testModelRequest(BaseModel):
    message: str

