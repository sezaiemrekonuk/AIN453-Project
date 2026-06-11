"""
Shared constants: tag map, grid geometry.
The total grid is 90 cm x 90 cm, and the lower-left corner is (0, 0).
8 AR tags — all same ID (0), asymmetric placement.
"""
import numpy as np

# 2-D tag positions in world frame [m]
TAG_POSITIONS = np.array([
    (0.33, 0.00),   # tag 0
    (0.50, 0.00),   # tag 1
    (0.90, 0.25),   # tag 2
    (0.90, 0.45),   # tag 3
    (0.00, 0.42),   # tag 4
    (0.00, 0.71),   # tag 5
    (0.05, 0.90),   # tag 6
    (0.55, 0.90),   # tag 7
], dtype=float)

TAG_SIZE = 0.065   # physical marker side length [m]  (6.5 cm)
TAG_Z    = 1.00   # tag center height [m] above floor

ROOM_X_MIN, ROOM_X_MAX = 0.0,  0.90
ROOM_Y_MIN, ROOM_Y_MAX = 0.0,  0.90

N_TAGS = len(TAG_POSITIONS)
