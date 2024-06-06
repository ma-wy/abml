#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/kyle/Documents/maws/lib")
from mwy_path_python3 import *
from mwy_lib_python3 import *
from hand_track.msg import hand_mp

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.hand_sub = rospy.Subscriber('/hand_msg', hand_mp, self.callback_hand)
#=======output==================================================================================
    self.hand_v_pub = rospy.Publisher("/hand_v", Float32, queue_size=1)
    self.if_hand_pub = rospy.Publisher("/if_hand", Int32, queue_size=1)
#===============================================================================================
# members
    self.hand_t_pre = rospy.get_time()
    self.hand_p_pre = array([0,0])
    self.hand_v = Float32()
    self.threshold = 10 #pix 40
    self.if_hand = 0
    
  def callback_hand(self, data):
    hand_t = data.header.stamp.to_sec()
    print(hand_t)
    index_tip = array([data.index_tip.x, data.index_tip.y])
    hand_d = norm(index_tip - self.hand_p_pre)
    if hand_d == 0:
      print('no hand is detected')
      self.hand_v.data = 0.0
      self.if_hand = 0
    elif hand_d < self.threshold:
      self.hand_v.data = 0.0
      self.if_hand = 1
      print('hand is not moving')
    elif hand_d > self.threshold:
      self.hand_v.data = hand_d/(hand_t - self.hand_t_pre)
      self.if_hand = 1
      print('hand is moving')
    print(self.hand_v.data)
    self.if_hand_pub.publish(self.if_hand)
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
    
    
