#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from controller_manager_msgs.srv import SwitchController, LoadController

# step 1
# roslaunch franka_human_friendly_controllers cartesian_variable_impedance_controller.launch robot_ip:=192.168.1.110 load_gripper:=True arm_id:=panda
# step 2
# rosrun move_franka test_switch_controller.py
# step 3
# rosrun rosrun controller_manager controller_manager list

rospy.init_node("test_switch_controller")
rospy.wait_for_service('/controller_manager/switch_controller')
switch_controller = rospy.ServiceProxy('/controller_manager/switch_controller', SwitchController)
#load_controller = rospy.ServiceProxy('/controller_manager/load_controller', LoadController)

#load_controller()
ret = switch_controller(start_controllers='cartesian_variable_impedance_controller', stop_controllers='position_joint_trajectory_controller', strictness=1, start_asap=True, timeout=0.0)
#ret = switch_controller(start_controllers='position_joint_trajectory_controller', stop_controllers='cartesian_variable_impedance_controller', strictness=1, start_asap=True, timeout=0.0)
#ret = switch_controller(start_controllers='position_joint_trajectory_controller', strictness=1, start_asap=True, timeout=0.0)
print(ret)
































    
    
    

