#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

rospy.init_node("rob_pose", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')
# move position with consistant orientation ########################
if len(sys.argv) == 8:
  p = sys.argv[1:4]
  q = sys.argv[4:8]
  pose = give_PoseStamped('panda_link0', q, p)
else:
  print('input 7d pose')
  p = [0.38976489273118314, 0.6127614453593411, 0.21634890199598963]
  q = [0.9718780980801518, -0.19555713120316162, -0.02780314088102366, 0.1282082534973701]   



  pose = give_PoseStamped('panda_link0', q, p)
  pose = rob.get_current_pose()
  print(pose)
  pose.pose.position.x = p[0]
  pose.pose.position.y = p[1]
  pose.pose.position.z = p[2]
  pose.pose.orientation.x = q[0]
  pose.pose.orientation.y = q[1]
  pose.pose.orientation.z = q[2]
  pose.pose.orientation.w = q[3]
  
  
  rob.go(pose)
    
    
    
    

