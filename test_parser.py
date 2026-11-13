
from services.tool_executor import execute_tool
from services.hardware_parser import parse_hardware_info

# Collect hardware information
hardware_data = {
    "cpu": execute_tool("cpu"),
    "memory": execute_tool("memory"),
    "storage": execute_tool("storage"),
    "gpu": execute_tool("gpu")
}

# Parse hardware information
result = parse_hardware_info(hardware_data)

# Print result
print(result)
