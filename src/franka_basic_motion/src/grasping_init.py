#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *


rospy.init_node("grasping_init", anonymous=True)
rob = MoveGroupCommander('panda_arm')
print(rob.set_end_effector_link('panda_hand_tcp'))
rob.set_max_velocity_scaling_factor(0.1)
rob.set_max_acceleration_scaling_factor(0.1)


if sys.argv[1] == 'handover':
# handover init pose #########################
  p = [0.289, 0.000, 0.400]
  q = [1.000, -0.002, -0.006, 0.002] 
  joints = [0, -50, 0, -150, 0, 100, 45]
  joints = deg_to_rad(joints)
  rob.go(joints)
elif sys.argv[1] == 'grasping':
# grasp init pose ###############################
  joints = [1.575267887668587, -0.4352075831555483, 0.26885588875151517, -2.2980965634335013, 0.15372256857881975, 1.6601492852899764, 1.0014479012643849]
  rob.go(joints)
else:
  print('No such action. Please try again.')
  print('Input the action name: 1. grasping, 2. handover')
    
    

