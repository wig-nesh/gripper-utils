import os
import urllib.request

GRIPPER_URL = (
    "https://raw.githubusercontent.com/wignesh/gripper-utils/main/assets/gripper.obj"
)


def get_cache_dir():
    path = os.path.expanduser("~/.cache/gripper-utils")
    os.makedirs(path, exist_ok=True)
    return path


def get_gripper_path():
    cache_dir = get_cache_dir()
    path = os.path.join(cache_dir, "gripper.obj")

    if not os.path.exists(path):
        print("[gripper-utils] Downloading gripper.obj...")
        urllib.request.urlretrieve(GRIPPER_URL, path)

    return path
