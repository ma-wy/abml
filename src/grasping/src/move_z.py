#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

rospy.init_node("move_z", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link("panda_hand")
pose = rob.get_current_pose()
target = pose.pose

target.position.z = target.position.z + 0.0
rob.go(pose)



    
    
    
    

