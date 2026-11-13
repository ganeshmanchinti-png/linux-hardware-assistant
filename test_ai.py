from services.ai_service import generate_ai_response
from services.tool_executor import execute_tool
from services.hardware_parser import parse_hardware_info

# Collect hardware information
hardware_data = {
    "cpu": execute_tool("cpu"),
    "memory": execute_tool("memory"),
    "storage": execute_tool("storage"),
    "gpu": execute_tool("gpu")
}

# Convert hardware information into readable text
hardware_info = parse_hardware_info(hardware_data)

# Ask AI a question
question = "What is my CPU and how many cores does it have?"

answer = generate_ai_response(question, hardware_info)

print("AI ANSWER:")
print(answer)