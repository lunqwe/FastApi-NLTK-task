from pydantic import BaseModel


# response schema for all endpoints
class ResponseSchema(BaseModel):
    text: str

