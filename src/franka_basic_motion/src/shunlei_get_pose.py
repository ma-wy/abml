#!/usr/bin/env python3.8

import sys
import rospy
from moveit_commander import MoveGroupCommander
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

# Initialize ROS node
rospy.init_node("get_current_pose", anonymous=True)

# Set up MoveGroup for the Panda arm
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')

# Explicitly set the reference frame for the pose
reference_frame = "panda_link0"
rob.set_pose_reference_frame(reference_frame)

# Get the current pose
current_pose = rob.get_current_pose().pose

# Extract position
x = current_pose.position.x
y = current_pose.position.y
z = current_pose.position.z

# Extract orientation (quaternion)
qx = current_pose.orientation.x
qy = current_pose.orientation.y
qz = current_pose.orientation.z
qw = current_pose.orientation.w

# Print the current pose in a single line format
print(f"{x:.4f}, {y:.4f}, {z:.4f}, {qx:.4f}, {qy:.4f}, {qz:.4f}, {qw:.4f}")

