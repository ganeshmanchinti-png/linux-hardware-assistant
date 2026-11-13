import json

from tools.cpu import get_cpu_info
from tools.memory import get_memory_info
from tools.storage import get_storage_info
from tools.gpu import get_gpu_info


def get_all_hardware_info():

    hardware_info = {
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "storage": get_storage_info(),
        "gpu": get_gpu_info()
    }

    return hardware_info


# Get all hardware information
hardware_data = get_all_hardware_info()

# Print complete hardware JSON
print(json.dumps(hardware_data, indent=4))

# Get all hardware information
hardware_data = get_all_hardware_info()

# Save hardware information into JSON file
with open("hardware.json", "w") as file:
    json.dump(hardware_data, file, indent=4)

print("Hardware information saved successfully!")