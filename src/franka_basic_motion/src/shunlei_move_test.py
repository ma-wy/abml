#!/usr/bin/env python3.8

import sys
import rospy
from moveit_commander import MoveGroupCommander
import tf
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

# Initialize ROS node
rospy.init_node("move_to_pose_with_constraints", anonymous=True)

# Set up MoveGroup for the Panda arm
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')
frame = "panda_link0"
rob.set_max_velocity_scaling_factor(0.1)
rob.set_max_acceleration_scaling_factor(0.1)
rob.set_planning_time(10.0)

# Get input arguments (position and quaternion)
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])
qx = float(sys.argv[4])
qy = float(sys.argv[5])
qz = float(sys.argv[6])
qw = float(sys.argv[7])

# Construct the target pose
target_position = [x, y, z]
target_orientation = [qx, qy, qz, qw]
target_pose = give_PoseStamped(frame, target_orientation, target_position)

# Get the current pose
current_pose = rob.get_current_pose().pose

# Calculate the position adjustment
adjusted_pose = current_pose
adjusted_pose.position.x += (target_pose.pose.position.x - current_pose.position.x)
adjusted_pose.position.y += (target_pose.pose.position.y - current_pose.position.y)
adjusted_pose.position.z += (target_pose.pose.position.z - current_pose.position.z)

# Calculate the orientation adjustment
current_orientation = [
    current_pose.orientation.x,
    current_pose.orientation.y,
    current_pose.orientation.z,
    current_pose.orientation.w
]

target_orientation = [
    target_pose.pose.orientation.x,
    target_pose.pose.orientation.y,
    target_pose.pose.orientation.z,
    target_pose.pose.orientation.w
]

# Interpolate between the current and target orientations (using spherical linear interpolation)
interpolated_orientation = tf.transformations.quaternion_slerp(
    current_orientation, target_orientation, 1.0
)

adjusted_pose.orientation.x = interpolated_orientation[0]
adjusted_pose.orientation.y = interpolated_orientation[1]
adjusted_pose.orientation.z = interpolated_orientation[2]
adjusted_pose.orientation.w = interpolated_orientation[3]

# Debug: Print the adjusted pose
print("Adjusted Pose:", adjusted_pose)

# Set the adjusted pose as the target
rob.set_pose_target(adjusted_pose)

# Plan and execute the movement
success = rob.go(wait=True)

# Stop the robot to ensure no residual motion
rob.stop()

# Clear the pose target to avoid issues with subsequent commands
rob.clear_pose_targets()

if success:
    print("Robot successfully moved to the adjusted pose.")
else:
    print("Failed to move the robot to the adjusted pose.")

