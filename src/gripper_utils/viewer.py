import os


def draw_geometries(geoms):
    os.environ["XDG_SESSION_TYPE"] = "x11"

    import open3d as o3d

    o3d.visualization.draw_geometries(geoms)
