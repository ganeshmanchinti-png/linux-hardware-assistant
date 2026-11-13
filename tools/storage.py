import subprocess
import json


def get_storage_info():

    result = subprocess.run(
        [
            "lsblk",
            "-b",
            "-J",
            "-o",
            "NAME,SIZE,TYPE,MOUNTPOINT,MODEL"
        ],
        capture_output=True,
        text=True,
        check=True,
        timeout=5
    )

    storage_data = json.loads(result.stdout)

    return storage_data["blockdevices"]