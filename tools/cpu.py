import subprocess


def get_cpu_info():

    result = subprocess.run(
        ["lscpu"],
        capture_output=True,
        text=True,
        check=True,
        timeout=5
    )

    cpu_data = {}

    for line in result.stdout.splitlines():

        if ":" in line:
            key, value = line.split(":", 1)

            cpu_data[key.strip()] = value.strip()

    return {
        "model_name": cpu_data.get("Model name"),
        "architecture": cpu_data.get("Architecture"),
        "cpu_cores": cpu_data.get("Core(s) per socket"),
        "threads": cpu_data.get("CPU(s)"),
        "vendor": cpu_data.get("Vendor ID")
    }