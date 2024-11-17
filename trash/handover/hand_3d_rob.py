#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.hand_sub = rospy.Subscriber('/hand_msg', hand_mp, self.callback_handedness)
    self.hand_pc_cam_sub = rospy.Subscriber('/hand_pc_cam', PointCloud2, self.callback_hand)
    self.camera_to_base_sub = rospy.Subscriber("/cam_to_base_tf", Pose, self.callback_camera_to_base)
#=======output==================================================================================
    self.hand_pc_pub = rospy.Publisher("/hand_pc_rob", PointCloud2, queue_size=10)
    self.hand_average_depth_pub = rospy.Publisher("/hand_average_depth", PointStamped, queue_size=10)
    self.hand_frame_pub = rospy.Publisher("/hand_frame", PoseStamped, queue_size=10)
#=================================================================================
    self.cam_to_base_p = zeros(3)
    self.cam_to_base_q = zeros(4)
    self.hand_average_xy = zeros(3)
    self.handedness = 'right'
    self.if_hand = Bool()
    self.if_hand.data = False
#===============================================================================================
# members
  def callback_camera_to_base(self, data):
    self.cam_to_base_p[0] = data.position.x
    self.cam_to_base_p[1] = data.position.y
    self.cam_to_base_p[2] = data.position.z
    self.cam_to_base_q[0] = data.orientation.x
    self.cam_to_base_q[1] = data.orientation.y
    self.cam_to_base_q[2] = data.orientation.z
    self.cam_to_base_q[3] = data.orientation.w

    
  def callback_handedness(self, data):
    self.handedness = data.handedness.data

  def callback_hand(self, data):
    r = 255
    g = 0
    b = 0
    a = 255
    rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
    trans = self.cam_to_base_p
    q_rot = self.cam_to_base_q
    hand_pc = []
    for pt in point_cloud2.read_points(data):
      p_cam = array([pt[0],pt[1],pt[2]])
      p_rob = list(transformation_P(p_cam,trans,q_rot))
      pt = p_rob + [rgb] # check
      hand_pc.append(pt)

    HEADER = Header()
    HEADER.frame_id = 'base'
    FIELDS = [
      PointField('x', 0, PointField.FLOAT32, 1),
      PointField('y', 4, PointField.FLOAT32, 1),
      PointField('z', 8, PointField.FLOAT32, 1),
      PointField('rgb', 12, PointField.UINT32, 1),
    ]
    POINTS = hand_pc#listhand_pc
    outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
    self.hand_pc_pub.publish(outputPoints)     
    
    # hand average depth
    self.hand_ad = give_PointStamped("base", hand_pc[-1][0:3])
    self.hand_average_depth_pub.publish(self.hand_ad)  


def main(args):
  rospy.init_node('hand_3d_rob', anonymous=True)
  rate = rospy.Rate(20)
  hd = hand_detect()

  
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

  main(sys.argv)
    
    
