#!/usr/bin/env python2.7
import sys 
sys.path.append("/home/mawanyu/MAws/lib")
from mwy_lib import *
from mwy_path import *
from hand_track.msg import hand_mp

class save_data:
  def __init__(self):
#=======input==================================================================================
    self.target_mod_sub = rospy.Subscriber('/rob_left_pose', PoseStamped, self.callback_rob_left)
    self.target_mod_sub = rospy.Subscriber('/rob_right_pose', PoseStamped, self.callback_rob_right)
    self.hand_mp_sub = rospy.Subscriber('/hand_msg', hand_mp, self.callback_hand_track)
    self.hand_v_sub = rospy.Subscriber('/hand_v', Float32, self.callback_v_hand)
    self.if_hand_sub = rospy.Subscriber('/if_hand', Int32, self.callback_if_hand)
# members
    self.left_ee_p = zeros(3)
    self.left_ee_q = zeros(4)
    self.right_ee_p = zeros(3)
    self.right_ee_q = zeros(4)
    self.hand = []
    self.hand_v = 0.0
    self.if_hand = 0

# functions
  def callback_if_hand(self,data):
    self.if_hand = data.data

  def callback_v_hand(self, data):
    self.hand_v = data.data

  def callback_hand_track(self,data):
    wrist = [int(data.wrist.x), int(data.wrist.y), data.wrist.z]
    thumb_tip = [int(data.thumb_tip.x), int(data.thumb_tip.y), data.thumb_tip.z]
    index_tip = [int(data.index_tip.x), int(data.index_tip.y), data.index_tip.z]
    middle_tip = [int(data.middle_tip.x), int(data.middle_tip.y), data.middle_tip.z]
    ring_tip = [int(data.ring_tip.x), int(data.ring_tip.y), data.ring_tip.z]
    pinky_tip = [int(data.pinky_tip.x), int(data.pinky_tip.y), data.pinky_tip.z]
    hand = wrist + thumb_tip + index_tip + middle_tip + ring_tip + pinky_tip
    self.hand = hand

  def callback_rob_left(self,data):
    self.left_ee_p[0] = data.pose.position.x
    self.left_ee_p[1] = data.pose.position.y
    self.left_ee_p[2] = data.pose.position.z
    self.left_ee_q[0] = data.pose.orientation.x
    self.left_ee_q[1] = data.pose.orientation.y
    self.left_ee_q[2] = data.pose.orientation.z
    self.left_ee_q[3] = data.pose.orientation.w   
    self.left_ee_p = list(self.left_ee_p)
    self.left_ee_q = list(self.left_ee_q)

  def callback_rob_right(self,data):
    self.right_ee_p[0] = data.pose.position.x
    self.right_ee_p[1] = data.pose.position.y
    self.right_ee_p[2] = data.pose.position.z
    self.right_ee_q[0] = data.pose.orientation.x
    self.right_ee_q[1] = data.pose.orientation.y
    self.right_ee_q[2] = data.pose.orientation.z
    self.right_ee_q[3] = data.pose.orientation.w 
    self.right_ee_p = list(self.right_ee_p)
    self.right_ee_q = list(self.right_ee_q)   

# class end=========================================================================================


def main(args):
  rospy.init_node('save_data', anonymous=True)
  sd = save_data()
  
  path = '/home/mawanyu/MAws/src/assembly/temp/data/'
  check_make_clear_folder(path)
  print "\n============ Press `Enter` to compute and save data ============"
  raw_input()
  while not rospy.is_shutdown():
    t = time.time()
    saveDataStep([t] + sd.left_ee_p, path+'left_ee_p.txt')
    saveDataStep([t] + sd.left_ee_q, path+'left_ee_q.txt')
    saveDataStep([t] + sd.right_ee_p, path+'right_ee_p.txt')
    saveDataStep([t] + sd.right_ee_q, path+'right_ee_q.txt')
    saveDataStep([t] + sd.hand, path+'hand.txt')
    saveDataStep([t] + [sd.if_hand, sd.hand_v], path+'hand_v.txt')
    rospy.sleep(0.5)

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
