#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------

# Debug: check ROS topics are available
sleep 2
echo "===== Available ROS Topics ====="
rostopic list || echo "rostopic unavailable"

# Launch particle filter localization with visualizer
dt-exec roslaunch pf_localization pf.launch run_visualizer:=true

# ----------------------------------------------------------------------------
# YOUR CODE ABOVE THIS LINE

# wait for app to end
dt-launchfile-join
