import numpy as np


def ang_to_vec(angles):
    assert angles.ndim == 1
    rads = np.deg2rad(angles)
    return np.column_stack((np.cos(rads), np.sin(rads)))


def vec_to_ang(vectors):
    assert vectors.ndim == 2 and vectors.shape[1] == 2
    return np.rad2deg(np.arctan2(vectors[:, 1], vectors[:, 0]))
