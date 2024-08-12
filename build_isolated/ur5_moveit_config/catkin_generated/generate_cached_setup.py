# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/noetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/noetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/abml/zoe_ws/devel_isolated/ur5_e_moveit_config;/home/abml/zoe_ws/devel_isolated/ur3_moveit_config;/home/abml/zoe_ws/devel_isolated/ur3_e_moveit_config;/home/abml/zoe_ws/devel_isolated/ur10_moveit_config;/home/abml/zoe_ws/devel_isolated/ur10_e_moveit_config;/home/abml/zoe_ws/devel_isolated/ur_description;/home/abml/zoe_ws/devel_isolated/ur_bringup;/home/abml/zoe_ws/devel_isolated/universal_robots;/home/abml/zoe_ws/devel_isolated/universal_robot;/home/abml/zoe_ws/devel_isolated/robotiq_arg85_description;/home/abml/zoe_ws/devel_isolated/pick-and-place;/home/abml/zoe_ws/devel_isolated/panda_robot;/home/abml/zoe_ws/devel_isolated/ndi_calibration;/home/abml/zoe_ws/devel_isolated/handover;/home/abml/zoe_ws/devel_isolated/gripper_force;/home/abml/zoe_ws/devel_isolated/grasping;/home/abml/zoe_ws/devel_isolated/franka_visualization;/home/abml/zoe_ws/devel_isolated/franka_tools;/home/abml/zoe_ws/devel_isolated/franka_ros_interface;/home/abml/zoe_ws/devel_isolated/franka_ros_controllers;/home/abml/zoe_ws/devel_isolated/franka_ros;/home/abml/zoe_ws/devel_isolated/franka_rocker_control;/home/abml/zoe_ws/devel_isolated/franka_realsense_calibration;/home/abml/zoe_ws/devel_isolated/franka_panda_description;/home/abml/zoe_ws/devel_isolated/franka_interface;/home/abml/zoe_ws/devel_isolated/franka_human_friendly_controllers;/home/abml/zoe_ws/devel_isolated/franka_gazebo;/home/abml/zoe_ws/devel_isolated/franka_example_controllers;/home/abml/zoe_ws/devel_isolated/franka_control;/home/abml/zoe_ws/devel_isolated/franka_hw;/home/abml/zoe_ws/devel_isolated/franka_core_msgs;/home/abml/zoe_ws/devel_isolated/franka_msgs;/home/abml/zoe_ws/devel_isolated/franka_moveit;/home/abml/zoe_ws/devel_isolated/franka_gripper;/home/abml/zoe_ws/devel_isolated/franka_description;/home/abml/zoe_ws/devel_isolated/air_pump;/home/abml/ndi_ws/devel;/home/abml/zoe_ws/devel;/home/abml/catkin_cl/devel;/opt/ros/noetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python3/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/abml/zoe_ws/devel_isolated/ur5_moveit_config/env.sh')

output_filename = '/home/abml/zoe_ws/build_isolated/ur5_moveit_config/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
