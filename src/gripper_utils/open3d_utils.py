from .assets import get_gripper_path


def load_gripper_mesh():
    import open3d as o3d

    path = get_gripper_path()
    return o3d.io.read_triangle_mesh(path)
