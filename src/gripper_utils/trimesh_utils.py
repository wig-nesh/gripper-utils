from .assets import get_gripper_path


def load_gripper_mesh():
    import trimesh

    path = get_gripper_path()
    return trimesh.load(path)
