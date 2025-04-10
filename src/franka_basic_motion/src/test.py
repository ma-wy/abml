#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

t1 = time.time()
rospy.init_node("get_rob_feedback", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')
print('ee_pose')
print(rob.get_current_pose())
print('joints in rad')
joints = rob.get_current_joint_values()
print(joints)

joint_index = int(1)
joint_value = deg_to_rad([float(80)])[0]
#joints[joint_index-1] += joint_value
t2 = time.time()
print(d_time_ms(t1, t2))
t1 = time.time()
#print('get_current_state_bounded')
#print(rob.get_current_state_bounded())?
joints[joint_index-1] -= joint_value
rob.go(joints,wait=False)
input()
rob.stop()
t2 = time.time()
print(d_time_ms(t1, t2))


