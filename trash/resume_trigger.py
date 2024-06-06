#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/kyle/Documents/maws/lib")
from mwy_path_python3 import *
from mwy_lib_python3 import *
from hand_track.msg import hand_mp

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.hand_v_sub = rospy.Subscriber('/hand_v', Float32, self.callback_hand)
#=======output==================================================================================
    self.stop_pub = rospy.Publisher("/resume_trigger", string, queue_size=1)
#===============================================================================================
# members
    self.hand_t_pre = rospy.get_time()
    self.hand_p_pre = array([0,0])
    self.hand_v = 
    self.threshold = 10 #pix 40
    
  def callback_v_hand(self, data):
    hand_t = data.header.stamp.to_sec()
    print(hand_t)
    index_tip = array([data.index_tip.x, data.index_tip.y])
    hand_d = norm(index_tip - self.hand_p_pre)
    if hand_d == 0:
      print('no hand is detected')
      self.hand_v.data = 0.0
    elif hand_d < self.threshold:
      self.hand_v.data = 0.0
      print('hand is not moving')
    elif hand_d > self.threshold:
      self.hand_v.data = hand_d/(hand_t - self.hand_t_pre)
      print('hand is moving')
    print(self.hand_v.data)
    self.hand_v_pub.publish(self.hand_v)
    self.hand_t_pre = hand_t
    self.hand_p_pre = index_tip
    
def main(args):
  rospy.init_node('hand_v_detect', anonymous=True)

  hd = hand_detect()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

  main(sys.argv)
    
    
