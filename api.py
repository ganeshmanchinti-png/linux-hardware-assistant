from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import ChatRequest, ChatResponse

from services.ai_service import generate_ai_response
from services.tool_executor import execute_tool
from services.hardware_parser import parse_hardware_info

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home API
@app.get("/")
def home():
    return {
        "message": "Linux Hardware Assistant API Running"
    }


# Get Hardware Information
@app.get("/hardware")
def get_hardware():

    hardware_data = {
        "cpu": execute_tool("cpu"),
        "memory": execute_tool("memory"),
        "storage": execute_tool("storage"),
        "gpu": execute_tool("gpu")
    }

    return hardware_data


# AI Chat API
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    hardware_data = {
        "cpu": execute_tool("cpu"),
        "memory": execute_tool("memory"),
        "storage": execute_tool("storage"),
        "gpu": execute_tool("gpu")
    }

    hardware_info = parse_hardware_info(hardware_data)

    answer = generate_ai_response(
        request.question,
        hardware_info
    )

    return ChatResponse(answer=answer)