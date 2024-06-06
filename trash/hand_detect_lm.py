#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/kyle/Documents/maws/lib")
from mwy_path_python3 import *
from mwy_lib_python3 import *
from leap_motion.msg import leap_mwy

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.hand_l_sub = rospy.Subscriber('/left_hand',leap_mwy, self.callback_hand_l, queue_size=2) 
    self.hand_r_sub = rospy.Subscriber('/right_hand',leap_mwy, self.callback_hand_r, queue_size=2) 
#=======output==================================================================================
#    self.rob_hand_cmd_left_pub = rospy.Publisher("/rob_hand_left",poseArray,queue_size=10)
#    self.rob_hand_cmd_right_pub = rospy.Publisher("/rob_hand_right",poseArray,queue_size=10)
#===============================================================================================
# members
    self.hand_l = []
    self.hand_r = []

  def callback_hand_l(self, data):
    print(data)
    
  def callback_hand_r(self, data):
    print(data)
    
      
 
            
def main(args):
  rospy.init_node('rob_hand_control', anonymous=True)

  hd = hand_detect()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
