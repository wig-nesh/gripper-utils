import numpy as np
import gripper_utils as gu


def main():
    print("📦 Testing gripper-utils...\n")

    print("--- 1. Testing Trimesh Loader ---")
    try:
        mesh_tm = gu.load_gripper_trimesh()
        print("✅ Trimesh loaded successfully!")
        print(f"   Type: {type(mesh_tm)}")
        print(f"   Vertices: {mesh_tm.vertices.shape}")
    except Exception as e:
        print(f"❌ Trimesh test failed: {e}")

    print("\n--- 2. Testing NumPy Backend ---")
    pts = np.random.rand(10, 3)
    T = np.eye(4)
    out_np = gu.transform_points(pts, T)
    print("✅ NumPy transform worked!")
    print(f"   Output type: {type(out_np)}")

    print("\n--- 3. Testing Mixed Backend (NumPy + Torch) ---")
    try:
        import torch

        T_torch = torch.eye(4)
        out_mixed = gu.transform_points(pts, T_torch)
        print("✅ Mixed transform worked (should have warned above)!")
        print(f"   Output type: {type(out_mixed)}")
    except ImportError:
        print("⚠️ PyTorch not installed, skipping mixed backend test.")

    print("\n--- 4. Testing Open3D Loader & Viewer ---")
    try:
        mesh_o3d = gu.load_gripper_open3d()
        print("✅ Open3D loaded successfully!")
        print(f"   Type: {type(mesh_o3d)}")
        print("   Opening visualization window (close the window to finish)...")
        gu.draw_geometries([mesh_o3d])
    except Exception as e:
        print(f"❌ Open3D test failed: {e}")


if __name__ == "__main__":
    main()
