#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

rospy.init_node("rot_joints", anonymous=True)
rob = MoveGroupCommander('panda_arm')
print(rob.set_end_effector_link('panda_hand_tcp'))
rob.set_max_velocity_scaling_factor(0.1)
rob.set_max_acceleration_scaling_factor(0.1)


joint_index = int(sys.argv[1])
joint_value = deg_to_rad([float(sys.argv[2])])[0]
print(joint_index)
print(joint_value)
if joint_index < 8 and joint_index > 0:
  joints = rob.get_current_joint_values()
  print('current joint values:')
  print(joints)
  joints[joint_index-1] = joint_value
  print('target joint values:')
  print(joints)
  rob.go(joints)
else:
  print('No such joint. Please try again.')
  print('Input the joint number from 1 to 7, where 1 represents base.')
    
    

