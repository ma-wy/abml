#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *



width = 0.032 #m


rospy.init_node("get_ee_pose", anonymous=True)
rob = MoveGroupCommander('panda_arm')

print(rob.get_current_pose())

    
    
    
    
