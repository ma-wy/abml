#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

rospy.init_node("trans_axis", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')
# move position with consistant orientation ########################
if len(sys.argv) == 3:
  axis = sys.argv[1]
  d = float(sys.argv[2])
elif len(sys.argv) == 4:
  axis = sys.argv[1]
  d = float(sys.argv[2])
  speed = float(sys.argv[3])
  rob.set_max_velocity_scaling_factor(speed)
  rob.set_max_acceleration_scaling_factor(speed)


pose = rob.get_current_pose()
target = pose.pose
if axis == 'x':
  target.position.x += d
elif axis == 'y':
  target.position.y += d
elif axis == 'z':
  target.position.z += d
rob.go(pose)
    
    
    
    

