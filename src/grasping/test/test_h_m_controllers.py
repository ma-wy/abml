#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from controller_manager_msgs.srv import SwitchController, LoadController
# test to run franka_human_friendly_controller and MoveGroupCommander at the same time

# step 1
# roslaunch franka_human_friendly_controllers cartesian_variable_impedance_controller.launch robot_ip:=192.168.1.110 load_gripper:=True arm_id:=panda
# step 2
# rosrun move_franka test_h_m_controller.py
# step 3
# rosrun rosrun controller_manager controller_manager list


rospy.init_node("test_h_m_controllers")
rospy.wait_for_service('/controller_manager/switch_controller')
switch_controller = rospy.ServiceProxy('/controller_manager/switch_controller', SwitchController)
# init
h = Panda()
m = MoveGroupCommander("panda_arm") #ee_link = panda_link8
ee_link_m = m.get_end_effector_link()

# control orientation via h
dr = 0.3
p_ee = h.curr_pos
q_orig = h.curr_q
q_rot = angle_axis_to_q([0,0,dr])
q_new = transformation_Q(q_orig,q_rot)
q_ee = list_2_quaternion(q_w_trans(q_new))
goal = array_quat_2_pose(p_ee, q_ee)
print("feedback from h")
print(p_ee) # [0.22035318 0.00104037 0.47687136]
print(q_orig)
print(q_ee)
# control position via m
dz = -0.05
pose = m.get_current_pose() # panda_link8
p_m, q_m = ee_pose_link8_to_ee(pose)
print("feedback from m")
print(p_m) 
print(q_m)
p_m[2] = p_m[2] + dz
print(p_m)
pose_target = give_Pose(p_m,q_m)
m.set_pose_target(pose_target, end_effector_link=ee_link_m)

# move
h.goal_pub.publish(goal)

switch_controller(start_controllers='position_joint_trajectory_controller', stop_controllers='cartesian_variable_impedance_controller', strictness=1, start_asap=True, timeout=0.0)
m.go(pose_target, wait=True)

switch_controller(start_controllers='cartesian_variable_impedance_controller', stop_controllers='position_joint_trajectory_controller', strictness=1, start_asap=True, timeout=0.0)
h.goal_pub.publish(goal)




































    
    
    

