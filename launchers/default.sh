#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------

# Launch particle filter localization (aruco_detector + particle_filter nodes).
# Add  run_visualizer:=true  to also start the matplotlib visualizer
# (requires a display — typically run separately on a laptop).
dt-exec roslaunch pf_localization pf.launch

# ----------------------------------------------------------------------------
# YOUR CODE ABOVE THIS LINE

# wait for app to end
dt-launchfile-join
