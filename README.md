# Particle Filter Localization with AR Tags — Duckiebot

ROS 1 (Noetic) dts package implementing a particle filter for real-time Duckiebot localization using ArUco tags.  
This is the **bonus real-robot port** of the simulation project. The Gazebo simulation lives in the sibling `Robotic-Project/` repo.

---

## Package overview

```
packages/pf_localization/
├── nodes/
│   ├── aruco_detector_node   — detects ArUco tags from compressed camera stream
│   ├── particle_filter_node  — SIR particle filter (predict + update + resample)
│   └── visualizer_node       — real-time matplotlib display (run on laptop)
├── src/pf_localization/
│   └── constants.py          — tag map, square grid bounds (edit to match physical setup)
├── launch/pf.launch           — wires all nodes with Duckiebot topic remaps
└── config/params.yaml         — tunable parameters
```

---

## Physical setup

Use the lower-left corner of the 90 cm x 90 cm grid as $(0, 0)$.

- **Grid**: x: 0.0..0.90 m, y: 0.0..0.90 m
- **Tags**: 8 × April Tag 36h11, placed asymmetrically:

| Tag | Position (x, y) | Wall |
|-----|----------------|------|
| T0  | (0.33, 0.00) | Bottom |
| T1  | (0.50, 0.00) | Bottom |
| T2  | (0.90, 0.25) | Right |
| T3  | (0.90, 0.45) | Right |
| T4  | (0.00, 0.42) | Left |
| T5  | (0.00, 0.71) | Left |
| T6  | (0.05, 0.90) | Top |
| T7  | (0.55, 0.90) | Top |

Tag centers at **1.0 m** height.  
If you change any position, update `src/pf_localization/constants.py` and `config/params.yaml`.

---

## Build

```bash
# From inside AIN453-Project/
dts devel build -f
```

Requires `dts` CLI and Docker. The build installs apt deps (`python3-opencv`, `python3-matplotlib`, `python3-numpy`) and runs `catkin build`.

---

## Run

### On the Duckiebot

```bash
dts devel run
```

This executes `launchers/default.sh` which calls:
```bash
roslaunch pf_localization pf.launch run_visualizer:=true
```

By default this starts `aruco_detector`, `particle_filter`, and the matplotlib visualizer.
If you need headless mode, run with `RUN_VISUALIZER=false`.

Topics:

| Topic | Direction | Description |
|-------|-----------|-------------|
| `/<veh>/camera_node/image/compressed` | in | Compressed camera frames |
| `/<veh>/camera_node/camera_info` | in | Camera intrinsics (auto-loaded) |
| `/<veh>/deadreckoning_node/odometry` | in | Odometry from deadreckoning |
| `/<veh>/ar_detection` | internal | Detected tag [distance, bearing] |
| `/<veh>/particles` | out | Particle cloud (PoseArray) |
| `/<veh>/pf_estimate` | out | Weighted-mean pose estimate |

If your odometry node publishes to a different topic, override at launch time:
```bash
roslaunch pf_localization pf.launch odom_topic:=/mybot/my_odom_node/odometry
```

### Visualizer (laptop)

The visualizer needs a display — run it on a laptop connected to the same ROS master:

```bash
export ROS_MASTER_URI=http://<VEHICLE_IP>:11311
roslaunch pf_localization pf.launch run_visualizer:=true
```

Or if the robot and laptop share a network and the package is built locally:
```bash
rosrun pf_localization visualizer_node \
  __name:=visualizer \
  ~particles:=/<veh>/particles \
  ~pf_estimate:=/<veh>/pf_estimate \
  ~odom:=/<veh>/deadreckoning_node/odometry
```

The visualizer shows:
- Room outline and all 8 tag positions (red squares)
- Particle cloud coloured by weight (plasma colormap)
- Odometry-only trajectory (blue)
- Particle filter estimate trajectory (green)

Screenshots are auto-saved to `~/pf_screenshots/` at three convergence milestones.

---

## Tuning parameters

Edit `config/params.yaml` or override via rosparam:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `n_particles` | 2000 | Number of particles |
| `sigma_dist` | 0.10 m | Distance measurement noise |
| `sigma_bear` | 0.08 rad | Bearing measurement noise |
| `alpha` | [0.10, 0.05, 0.05, 0.02] | Odometry noise (a1..a4) |
| `tag_size` | 0.25 m | Physical marker side length |

Increase `sigma_dist` / `sigma_bear` if the filter collapses early. Decrease them once the physical setup is accurate and the camera is calibrated.

---

## Camera calibration

The ArUco detector subscribes to `~camera_info` and loads the intrinsic matrix automatically from the camera node. No manual calibration entry is needed if the Duckiebot camera node is running.

If camera_info is unavailable, the node falls back to approximate defaults:
- fx = fy = 302, cx = 320, cy = 240 (OV5647, 640×480)

For best results, run the Duckietown camera calibration procedure first.

---

## Sensor model note

The detector publishes **horizontal distance** `sqrt(X² + Z²)` from the ArUco `solvePnP` result, not the raw 3D distance. This is consistent with the particle filter's sensor model which uses 2D tag positions — no height correction parameter needed.

---

## Dependencies

- ROS Noetic (`dt-ros-commons:daffy` base image)
- OpenCV with aruco (Ubuntu 20.04 `python3-opencv` includes contrib)
- numpy, matplotlib

Both old (≤4.6) and new (≥4.7) OpenCV aruco APIs are supported automatically.
