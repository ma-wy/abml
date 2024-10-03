#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

class grasp_move:
  def __init__(self):
#=======input==================================================================================
    self.grasp_target_sub = rospy.Subscriber("/grasp_target", PoseArray, self.callback_grasp_target)
#=======output====================================================================================
# members
    self.target = []
# functions
  def callback_grasp_target(self,data):
    poses = data.poses
    pose_target_list = []
    for pose in poses:
      target = get_Pose(pose)
      p = target[0:3]
      ra = q_to_angle_axis(array(target[3:7]))
      pose_target = np.concatenate((p,ra)) 
      pose_target_list.append(pose_target)
    self.target = pose_target_list  
# class end=========================================================================================

def main(args):
  rospy.init_node('grasp_move', anonymous=True)
  gm = grasp_move()
  rob = urx.Robot("169.254.162.54")
  rob.set_tcp((0, 0, 0.265, 0, 0, 0))
  rob.set_payload(2, (0, 0, 0.1))
  a = 0.2
  v = 0.3 
  time.sleep(5)
  print('target list length: ' + str(len(gm.target)))
  print("press 'enter' to check target")
  #input()
  target_list = gm.target
  for pose in target_list:
    rob.movel(pose,a,v)
  rob.close()


if __name__ == '__main__':

    main(sys.argv)
