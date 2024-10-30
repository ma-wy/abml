#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

class move_franka(Panda):
    def __init__(self):
      super(move_franka, self).__init__()
#input==============================================================================================      
      self.goal_sub = rospy.Subscriber('/position_goal', Float64MultiArray, self.callback_position_goal)
      self.rob = MoveGroupCommander('panda_arm')
      self.rob.set_end_effector_link("panda_hand")
      pose = self.rob.get_current_pose()
      self.target = pose.pose


    def callback_position_goal(self, data):
      pose = self.rob.get_current_pose()
      self.target = pose.pose
      p = data.data
      self.target.position.x = p[0]
      self.target.position.y = p[1]
      self.target.position.z = p[2]
      rob.go(self.target)
      

def main(args):
  rospy.init_node("move_method_2", anonymous=True)
  mf = move_franka()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    






    
    
    
    

