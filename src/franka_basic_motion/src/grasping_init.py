#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from franka_utils import *


rospy.init_node("grasping_init", anonymous=True)


magnet_pub = rospy.Publisher("/control_magnet", Int32, queue_size=1)
power_pub = rospy.Publisher("/control_power", Int32, queue_size=1)
magnet_trigger = Int32()
power_trigger = Int32()
power_trigger.data = 0
#power_pub.publish(power_trigger)
magnet_trigger.data = 0
#magnet_pub.publish(magnet_trigger)



rob = MoveGroupCommander('panda_arm')
print(rob.set_end_effector_link('panda_hand_tcp'))
rob.set_max_velocity_scaling_factor(0.1)
rob.set_max_acceleration_scaling_factor(0.1)

gripper_move_client = actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction)
gripper_move_client.wait_for_server()  
print('open the gripper')
b = franka_open_gripper(client=gripper_move_client, width=0.02, speed=0.1)
print(b)


if sys.argv[1] == 'handover':
# handover init pose #########################
  p = [0.289, 0.000, 0.400]
  q = [1.000, -0.002, -0.006, 0.002] 
  joints = [0, -50, 0, -150, 0, 100, 45]
  joints = deg_to_rad(joints)
  rob.go(joints)
elif sys.argv[1] == 'grasping':
# grasp init pose ###############################
#  joints = [1.5329898920017373, -0.4312032256502854, 0.20277807849750182, -2.314865548489653, 0.10410149058684617, 1.6572950763437482, 0.9102000554130256]
  joints = grasping_pose_init # defined in mwy_lib 
  rob.go(joints)
elif sys.argv[1] == 'counting':  
  joints = counting_pose_init # defined in mwy_lib 
  rob.go(joints)  
elif sys.argv[1] == 'tempt':  
  joints = tempt_pose_init # defined in mwy_lib 
  rob.go(joints)  
else:
  print('No such action. Please try again.')
  print('Input the action name: 1. grasping, 2. handover')

