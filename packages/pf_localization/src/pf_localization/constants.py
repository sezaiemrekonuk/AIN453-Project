"""
Shared constants: tag map, room geometry.
Room: 6 m x 5 m  (x: -3.0..+3.0,  y: -2.5..+2.5)
8 AR tags — all same ID (0), asymmetric placement.
"""
import numpy as np

# 2-D tag positions in world frame [m]
TAG_POSITIONS = np.array([
    (-1.50, -2.46),   # tag 0  South-Left
    ( 1.20, -2.46),   # tag 1  South-Right
    (-0.30,  2.46),   # tag 2  North-Left
    ( 2.00,  2.46),   # tag 3  North-Right
    (-2.96, -0.50),   # tag 4  West-Bottom
    (-2.96,  1.50),   # tag 5  West-Top
    ( 2.96,  0.50),   # tag 6  East-Top
    ( 2.96, -1.50),   # tag 7  East-Bottom
], dtype=float)

TAG_SIZE = 0.25   # physical marker side length [m]
TAG_Z    = 1.00   # tag center height [m] above floor

ROOM_X_MIN, ROOM_X_MAX = -3.0,  3.0
ROOM_Y_MIN, ROOM_Y_MAX = -2.5,  2.5

N_TAGS = len(TAG_POSITIONS)
