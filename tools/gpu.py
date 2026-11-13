import subprocess


def get_gpu_info():

    result = subprocess.run(
        ["lspci"],
        capture_output=True,
        text=True,
        check=True,
        timeout=5
    )

    gpu_list = []

    for line in result.stdout.splitlines():

        if any(
            keyword in line.lower()
            for keyword in ["vga", "3d controller", "display controller"]
        ):
            gpu_list.append(line.strip())

    return gpu_list