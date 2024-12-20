#!/usr/bin/env python3.8

import sys
import os
import rospy
import numpy as np
import cv2
import pyrealsense2 as rs
from moveit_commander import MoveGroupCommander
from tf.transformations import euler_from_quaternion
import time as tm

sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

# Robot and camera configuration
output_path = "/home/abml/sl_data_collector/franka/data"
data_filename = 'collected_data.npy'
video_filename = 'collected_video.avi'

# Initialize ROS node
rospy.init_node("data_collection_with_camera", anonymous=True)

# Set up MoveGroup for the Panda arm and gripper
arm = MoveGroupCommander('panda_arm')
arm.set_end_effector_link('panda_hand_tcp')
gripper = MoveGroupCommander('panda_hand')

# Configure RealSense color stream
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
video_writer = cv2.VideoWriter(os.path.join(output_path, video_filename), fourcc, fps, (224, 224))  # Video size adjusted for future resize

# Data collection variables
data = {
    "robot_state": [],
    "action": [],
    "color_image": []
}

last_save_time = tm.time()

def crop_and_resize(image, target_size=(224, 224), resize=False):
    """
    Crop the image to a square (center crop) and optionally resize to the target size.

    Args:
        image (np.ndarray): The input image.
        target_size (tuple): The desired output size (height, width).
        resize (bool): Whether to resize after cropping.

    Returns:
        np.ndarray: The cropped (and optionally resized) image.
    """
    height, width, _ = image.shape
    min_dim = min(height, width)

    # Compute cropping box (center crop)
    start_x = (width - min_dim) // 2
    start_y = (height - min_dim) // 2
    cropped_image = image[start_y:start_y + min_dim, start_x:start_x + min_dim]

    if resize:
        # Resize to the target size
        cropped_image = cv2.resize(cropped_image, target_size)
        # Commented resize functionality:
        # return cv2.resize(cropped_image, target_size)

    return cropped_image

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

try:
    # Initialize the previous pose and gripper state
    previous_pose = get_current_pose()
    previous_gripper_state = get_gripper_state()
    gripper_action = 0
    i = 0

    rospy.loginfo("Data collection started. Press 'q' to stop.")

    while not rospy.is_shutdown():
        # Capture frames from RealSense
        frames = pipeline.wait_for_frames(timeout_ms=10000)  # 10 seconds timeout
        color_frame = frames.get_color_frame()

        if not color_frame:
            rospy.logwarn("Failed to retrieve color frame from RealSense camera.")
            continue

        # Convert color frame to numpy array
        color_image = np.asanyarray(color_frame.get_data())

        # Crop (without resizing) the image
        cropped_image = crop_and_resize(color_image, target_size=(224, 224), resize=False)

        # Get current state
        current_pose = get_current_pose()
        current_gripper_state = get_gripper_state()

        # Update gripper action
        if current_gripper_state != previous_gripper_state:
            gripper_action = current_gripper_state

        # Compute deltas
        delta_xyz, delta_rpy = compute_deltas(previous_pose, current_pose)
        action = delta_xyz + delta_rpy + [gripper_action]

        # Append data
        data["robot_state"].append(current_pose + [0, current_gripper_state])
        data["action"].append(action)
        data["color_image"].append(cropped_image)

        # Save video frame
        video_writer.write(cropped_image)

        # Display cropped image
        cv2.imshow("RealSense", cropped_image)

        # Log information
        rospy.loginfo(f"Captured State_{i}: {data['robot_state'][-1]}")
        rospy.loginfo(f"Captured Action_{i}: {data['action'][-1]}")

        # Update previous state
        previous_pose = current_pose
        previous_gripper_state = current_gripper_state
        i += 1

        # Check for 'q' key press to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            rospy.loginfo("Data collection stopped by user.")
            break

finally:
    # Convert lists to numpy arrays
    data["robot_state"] = np.array(data["robot_state"])
    data["action"] = np.array(data["action"])
    data["color_image"] = np.array(data["color_image"])

    # Save data and release resources
    np.save(os.path.join(output_path, data_filename), data)
    video_writer.release()
    pipeline.stop()
    cv2.destroyAllWindows()
    rospy.loginfo(f"Data saved to {os.path.join(output_path, data_filename)}")

