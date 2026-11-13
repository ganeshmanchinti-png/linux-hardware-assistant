
def parse_hardware_info(hardware_data):

    cpu = hardware_data["cpu"]
    memory = hardware_data["memory"]
    storage = hardware_data["storage"]
    gpu = hardware_data["gpu"]

    # Convert bytes into GB
    total_ram = round(memory["total_bytes"] / (1024 ** 3), 2)
    used_ram = round(memory["used_bytes"] / (1024 ** 3), 2)
    free_ram = round(memory["free_bytes"] / (1024 ** 3), 2)

    # Create readable hardware information
    result = f"""
HARDWARE INFORMATION

CPU:
Model: {cpu["model_name"]}
Architecture: {cpu["architecture"]}
Cores: {cpu["cpu_cores"]}
Threads: {cpu["threads"]}

MEMORY:
Total RAM: {total_ram} GB
Used RAM: {used_ram} GB
Free RAM: {free_ram} GB

STORAGE:
"""

    for disk in storage:
        size_gb = round(disk["size"] / (1024 ** 3), 2)

        result += f"""
Name: {disk["name"]}
Size: {size_gb} GB
Type: {disk["type"]}
Mountpoint: {disk["mountpoint"]}
"""

    result += "\nGPU:\n"

    for item in gpu:
        result += f"{item}\n"

    return result
