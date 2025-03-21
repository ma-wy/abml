#!/usr/bin/env python3.8

import sys
import rospy
import numpy as np
from moveit_commander import MoveGroupCommander
from tf.transformations import euler_from_quaternion
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

# Initialize ROS node
rospy.init_node("data_collection_with_delta_tracking", anonymous=True)

# Set up MoveGroup for the Panda arm and gripper
arm = MoveGroupCommander('panda_arm')
arm.set_end_effector_link('panda_hand_tcp')
gripper = MoveGroupCommander('panda_hand')

# List to store collected data
data_list = []

# Output file name
output_file = "/home/abml/sl_data_collector/franka/data/states_actions3.npy"

def get_current_pose():
    """Returns the current position (x, y, z) and orientation (roll, pitch, yaw) of the end-effector."""
    current_pose = arm.get_current_pose().pose

    # Extract position
    x = current_pose.position.x
    y = current_pose.position.y
    z = current_pose.position.z

    # Extract orientation and convert to Roll-Pitch-Yaw
    qx = current_pose.orientation.x
    qy = current_pose.orientation.y
    qz = current_pose.orientation.z
    qw = current_pose.orientation.w
    roll, pitch, yaw = euler_from_quaternion([qx, qy, qz, qw])

    return [x, y, z, roll, pitch, yaw]

def get_gripper_state():
    """Returns the current gripper state (0 for open, 1 for closed)."""
    return 1 if gripper.get_current_joint_values()[0] < 0.02 else 0

def compute_deltas(previous_pose, current_pose):
    """Computes delta position (xyz) and delta orientation (rpy) between two poses."""
    # Delta position
    delta_x = current_pose[0] - previous_pose[0]
    delta_y = current_pose[1] - previous_pose[1]
    delta_z = current_pose[2] - previous_pose[2]

    # Delta orientation (Roll-Pitch-Yaw)
    delta_roll = current_pose[3] - previous_pose[3]
    delta_pitch = current_pose[4] - previous_pose[4]
    delta_yaw = current_pose[5] - previous_pose[5]

    return [delta_x, delta_y, delta_z], [delta_roll, delta_pitch, delta_yaw]

def collect_data():
    rospy.loginfo("Data collection started. Press Ctrl+C to stop.")

    # Initialize the previous pose and gripper state
    previous_pose = get_current_pose()
    previous_gripper_state = get_gripper_state()

    # Initialize gripper action (0 = idle/open state initially)
    gripper_action = 0

    rate = rospy.Rate(5)  # 5 Hz

    while not rospy.is_shutdown():
        try:
            # Get the current state
            current_pose = get_current_pose()
            current_gripper_state = get_gripper_state()

            # Update gripper action logic:
            # - If gripper is moving from open to closed, set action to 1
            # - If gripper is moving from closed to open, set action to 0
            if current_gripper_state != previous_gripper_state:
                gripper_action = current_gripper_state

            # Construct the state and action data
            state = current_pose + [0, current_gripper_state]  # [x, y, z, roll, pitch, yaw, <PAD>, gripper_state]
            delta_xyz, delta_rpy = compute_deltas(previous_pose, current_pose)
            action = delta_xyz + delta_rpy + [gripper_action]  # [delta_x, delta_y, delta_z, delta_roll, delta_pitch, delta_yaw, gripper_action]

            # Save state and action as a tuple in the data list
            data_list.append([state, action])

            # Log the data for debugging
            rospy.loginfo(f"State: {state}, Action: {action}")

            # Update the previous pose and gripper state
            previous_pose = current_pose
            previous_gripper_state = current_gripper_state

            # Sleep to control the loop rate
            rate.sleep()

        except Exception as e:
            rospy.logerr(f"Error during data collection: {e}")
            break

    # Convert the data list to a NumPy array
    data_array = np.array(data_list, dtype=object)

    # Save the array as a .npy file
    np.save(output_file, data_array)
    rospy.loginfo(f"Data successfully saved to {output_file}")

if __name__ == "__main__":
    try:
        collect_data()
    except rospy.ROSInterruptException:
        rospy.loginfo("Data collection interrupted.")

