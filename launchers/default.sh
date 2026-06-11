#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------

# Launch particle filter localization.
# By default, the visualizer is enabled so `dts devel run` can open it directly
# on a machine with a forwarded display. Set RUN_VISUALIZER=false to disable it.
RUN_VISUALIZER="${RUN_VISUALIZER:-true}"
dt-exec roslaunch pf_localization pf.launch run_visualizer:=${RUN_VISUALIZER}

# ----------------------------------------------------------------------------
# YOUR CODE ABOVE THIS LINE

# wait for app to end
dt-launchfile-join
