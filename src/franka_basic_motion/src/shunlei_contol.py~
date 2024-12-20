#!/usr/bin/env python3.8

import sys
import rospy
from moveit_commander import MoveGroupCommander
from std_msgs.msg import Int32, Float64  # Import required message types
import tf
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

# Initialize ROS node
rospy.init_node("robot_control", anonymous=True)

# Set up MoveGroup for the Panda arm and gripper
arm = MoveGroupCommander('panda_arm')
gripper = MoveGroupCommander('panda_hand')

# Configure arm parameters
arm.set_end_effector_link('panda_hand_tcp')
arm.set_max_velocity_scaling_factor(0.1)
arm.set_max_acceleration_scaling_factor(0.1)
arm.set_planning_time(10.0)

# Configure gripper parameters
gripper.set_goal_joint_tolerance(0.002)

# Define poses for different actions  
poses = {
    'initial': {'position': [-0.1136, 0.5342, 0.3186], 'orientation': [-0.7288, -0.6829, -0.0242, 0.0442]},
    #instrument 1
#    'grasp': {'position': [-0.3201, 0.4693, -0.0492], 'orientation': [0.6963, 0.7173, -0.0157, 0.0200]},
#    'safe': {'position': [-0.3200, 0.4767, -0.0021], 'orientation': [-0.7012, -0.7125, 0.0022, 0.0266]},
    
    #instrument 2
#    'grasp': {'position': [-0.2275, 0.4714, -0.0488], 'orientation': [-0.7057, -0.7085, 0.0094, 0.0056]},
 #   'safe': {'position': [-0.2326, 0.4694, -0.0146], 'orientation': [-0.7151, -0.6985, -0.0250, 0.0108]},
    
    #instrument 3
#    'grasp': {'position': [-0.1581, 0.4817, -0.0495], 'orientation': [0.7220, 0.6912, -0.0280, 0.0103]},
#    'safe': {'position': [-0.1543, 0.4889, -0.0079], 'orientation': [-0.7205, -0.6933, 0.0119, 0.0086]},

    #instrument 4
#    'grasp': {'position': [-0.0647, 0.4831, -0.0497], 'orientation': [0.7050, 0.7084, -0.0331, 0.0068]},
#    'safe': {'position': [-0.0651, 0.4878, -0.0165], 'orientation': [-0.7069, -0.7068, 0.0265, 0.0010]},
    
    #instrument 5
    'grasp': {'position': [0.0095, 0.4989, -0.0543], 'orientation': [-0.7178, -0.6960, 0.0179, 0.0087]},
    'safe': {'position': [0.0111, 0.5153, 0.0194], 'orientation': [-0.7231, -0.6901, 0.0160, 0.0244]},

    #instrument 6
#    'grasp': {'position': [0.1141, 0.4860, -0.0514], 'orientation': [0.6788, 0.7338, -0.0260, 0.0012]},
#    'safe': {'position': [0.1201, 0.5004, -0.0055], 'orientation': [0.6787, 0.7341, -0.0204, 0.0011]},

    #handover 1
#   'handover': {'position': [0.3474, 0.4672, -0.0379], 'orientation': [-0.9899, 0.1337, 0.0429, 0.0178]}
    #handover 2
    'handover': {'position': [0.1245, 0.4958, 0.0281], 'orientation': [1.0000, -0.0043, -0.0020, 0.0051]}
    #handover 3
#    'handover': {'position': [0.3267 0.6848, -0.0312], 'orientation': [-0.9880, -0.1467, -0.0194, 0.0451]}
}
 

# Gripper widths
gripper_widths = {
    'open': 0.025,  # Per finger joint (0.05 total width)
    'close': 0.001  # Nearly fully closed
}

# Publishers for additional gripper actions
magnet_pub = rospy.Publisher('/control_magnet', Int32, queue_size=10)
pump_pub = rospy.Publisher('/control_pump', Float64, queue_size=10)
power_pub = rospy.Publisher('/control_power', Int32, queue_size=10)

# Function to move the arm to a named pose
def move_to_pose(pose_name):
    if pose_name not in poses:
        rospy.logwarn(f"Pose '{pose_name}' not defined.")
        return False
    
    # Get the target pose
    pose = poses[pose_name]
    target_pose = give_PoseStamped('panda_link0', pose['orientation'], pose['position'])

    # Get the current pose
    current_pose = arm.get_current_pose().pose

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

    # Interpolate between the current and target orientations
    interpolated_orientation = tf.transformations.quaternion_slerp(
        current_orientation, target_orientation, 1.0
    )

    adjusted_pose.orientation.x = interpolated_orientation[0]
    adjusted_pose.orientation.y = interpolated_orientation[1]
    adjusted_pose.orientation.z = interpolated_orientation[2]
    adjusted_pose.orientation.w = interpolated_orientation[3]

    # Debug: Print the adjusted pose
    rospy.loginfo(f"Adjusted Pose: {adjusted_pose}")

    # Set the adjusted pose as the target
    arm.set_pose_target(adjusted_pose)

    # Plan and execute the movement
    success = arm.go(wait=True)
    arm.stop()
    arm.clear_pose_targets()

    if success:
        rospy.loginfo(f"Moved to '{pose_name}' pose.")
    else:
        rospy.logwarn(f"Failed to move to '{pose_name}' pose.")
    return success

# Function to control gripper-specific actions
def control_gripper(action):
    if action == 'magon':
        rospy.loginfo("Activating magnet, pump, and power.")
        magnet_pub.publish(Int32(1))  # Activate the magnet
        rospy.sleep(0.1)
        pump_pub.publish(Float64(3.8))  # Set pump pressure
        rospy.sleep(0.1)
        power_pub.publish(Int32(1))  # Enable power
        rospy.sleep(0.1)
    elif action == 'magoff':
        rospy.loginfo("Deactivating magnet and power.")
        magnet_pub.publish(Int32(0))  # Deactivate the magnet
        rospy.sleep(0.1)
        power_pub.publish(Int32(0))  # Disable power
        rospy.sleep(0.1)
    elif action in gripper_widths:
        width = gripper_widths[action]
        rospy.loginfo(f"{'Opening' if action == 'open' else 'Closing'} the gripper...")
        success = gripper.go([width, width], wait=True)
        gripper.stop()
        if success:
            rospy.loginfo(f"Gripper '{action}' action completed.")
        else:
            rospy.logwarn(f"Gripper '{action}' action failed.")
    else:
        rospy.logwarn(f"Invalid gripper action '{action}'.")

# Main loop
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            # Get user input
            action = input("Enter action (i: initial, g: grasp, c: close gripper, o: open gripper, s: safe, h: handover, magon: activate magnet, magoff: deactivate magnet, q: quit): ").strip().lower()
            
            if action == 'i':
                move_to_pose('initial')
            elif action == 'g':
                move_to_pose('grasp')
            elif action == 'c':
                control_gripper('close')
            elif action == 'o':
                control_gripper('open')
            elif action == 's':
                move_to_pose('safe')
            elif action == 'h':
                move_to_pose('handover')
            elif action == 'magon':
                control_gripper('magon')
            elif action == 'magoff':
                control_gripper('magoff')
            elif action == 'q':
                rospy.loginfo("Exiting robot control.")
                break
            else:
                rospy.logwarn("Invalid input. Please enter a valid command.")
    except rospy.ROSInterruptException:
        pass

