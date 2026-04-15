import warnings


def is_numpy(x):
    return type(x).__module__.startswith("numpy")


def is_torch(x):
    return type(x).__module__.startswith("torch")


def detect_backend(*args):
    has_np = any(is_numpy(a) for a in args)
    has_torch = any(is_torch(a) for a in args)

    if has_np and has_torch:
        warnings.warn(
            "[gripper-utils] Mixed NumPy and Torch inputs. Converting all to Torch."
        )
        import torch

        converted = [torch.from_numpy(a) if is_numpy(a) else a for a in args]
        return torch, converted

    elif has_torch:
        import torch

        return torch, args

    else:
        import numpy as np

        return np, args


def transform_points(points, transform):
    xp, (points_conv, transform_conv) = detect_backend(points, transform)

    # assume points: (N, 3), transform: (4, 4)
    ones = xp.ones((points_conv.shape[0], 1))

    # Needs handling since torch.concatenate is cat, np is concatenate.
    # To be perfectly safe, let's use the appropriate concat function based on backend.
    if xp.__name__ == "torch":
        ones = xp.ones(
            (points_conv.shape[0], 1),
            dtype=points_conv.dtype,
            device=points_conv.device,
        )
        points_h = xp.cat([points_conv, ones], dim=1)
        if points_h.dtype != transform_conv.dtype:
            points_h = points_h.to(transform_conv.dtype)
    else:
        ones = xp.ones((points_conv.shape[0], 1), dtype=points_conv.dtype)
        points_h = xp.concatenate([points_conv, ones], axis=1)

    transformed = (transform_conv @ points_h.T).T[:, :3]

    return transformed
