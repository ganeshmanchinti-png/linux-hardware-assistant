
from tools.cpu import get_cpu_info
from tools.memory import get_memory_info
from tools.storage import get_storage_info
from tools.gpu import get_gpu_info


def execute_tool(tool_name):

    if tool_name == "cpu":
        return get_cpu_info()

    elif tool_name == "memory":
        return get_memory_info()

    elif tool_name == "storage":
        return get_storage_info()

    elif tool_name == "gpu":
        return get_gpu_info()

    else:
        return {"error": "Tool not found"}
