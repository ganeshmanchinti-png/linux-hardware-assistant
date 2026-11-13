import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import ChatRequest, ChatResponse
from services.ai_service import generate_ai_response
from services.tool_executor import execute_tool

app = FastAPI()

frontend_url = os.getenv(
    "FRONTEND_URL",
    "http://localhost:5173"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        frontend_url
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Linux Hardware Assistant API Running"
    }


@app.get("/hardware")
def get_hardware():
    return {
        "cpu": execute_tool("cpu"),
        "memory": execute_tool("memory"),
        "storage": execute_tool("storage"),
        "gpu": execute_tool("gpu")
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = generate_ai_response(request.question)

    return ChatResponse(answer=answer)
