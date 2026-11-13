
from pydantic import BaseModel


# User question schema
class ChatRequest(BaseModel):
    question: str


# AI response schema
class ChatResponse(BaseModel):
    answer: str
