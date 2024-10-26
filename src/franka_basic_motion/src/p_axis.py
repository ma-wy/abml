#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

rospy.init_node("p_axis", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')
# move position with consistant orientation ########################
axis = sys.argv[1]
p = float(sys.argv[2])

pose = rob.get_current_pose()
target = pose.pose
if axis == 'x':
  target.position.x = p
elif axis == 'y':
  target.position.y = p
elif axis == 'z':
  target.position.z = p
rob.go(pose)
    
    
    
    

