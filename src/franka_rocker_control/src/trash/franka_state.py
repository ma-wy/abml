#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *

class franka_state:
  def __init__(self):
#=======input========================position==========================================================
    self.time_origin_sub = rospy.Subscriber('/time_origin', Float32, self.callback_time_origin)
#=======output==================================================================================
    self.rob_ee_pub = rospy.Publisher('/rob_ee', PoseStamped, queue_size=1)
#===============================================================================================
# members
    self.base_frame = 'panda_link0'
    self.ee_frame = 'panda_hand_tcp'
    self.listener = tf.TransformListener()
    self.listener.waitForTransform(self.base_frame, self.ee_frame,rospy.Time(), rospy.Duration(40.0))
    (self.ee_p, self.ee_q) = self.listener.lookupTransform(self.base_frame, self.ee_frame, rospy.Time(0))
 
# functions
  def callback_time_origin(self, data):
    (self.ee_p,self.ee_q) = self.listener.lookupTransform(self.base_frame, self.ee_frame, rospy.Time(0))
    ee_pose_pub = give_PoseStamped(self.base_frame, self.ee_q, self.ee_p)
    self.rob_ee_pub.publish(ee_pose_pub)
    
# class end=========================================================================================
def main(args):
  rospy.init_node('franka_state', anonymous=True)
  fs = franka_state()
 
  try:
    rospy.spin()

  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)

