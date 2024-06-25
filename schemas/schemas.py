from pydantic import BaseModel


# response schema for all endpoints
class RequestSchema(BaseModel):
    text: str

