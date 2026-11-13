import subprocess


def get_memory_info():

    result = subprocess.run(
        ["free", "-b"],
        capture_output=True,
        text=True,
        check=True,
        timeout=5
    )

    lines = result.stdout.splitlines()

    memory_line = None

    for line in lines:
        if line.startswith("Mem:"):
            memory_line = line.split()
            break

    return {
        "total_bytes": int(memory_line[1]),
        "used_bytes": int(memory_line[2]),
        "free_bytes": int(memory_line[3]),
        "available_bytes": int(memory_line[6])
    }