#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.hand_sub = rospy.Subscriber('/hand_msg', hand_mp, self.callback_hand)
    self.image2_sub = message_filters.Subscriber('/camera_top/aligned_depth_to_color/image_raw', Image)#, queue_size=2
    self.image2_sub.registerCallback(self.callback_image2) 
    self.rgb_sub = message_filters.Subscriber('/camera_top/color/image_raw', Image)
    self.rgb_sub.registerCallback(self.callback_rgb) 
#=======output==================================================================================
    self.hand_pc_pub = rospy.Publisher("/hand_pc_cam",PointCloud2,queue_size=10)
    self.img_pc_pub = rospy.Publisher("/downsampled_pc",PointCloud2,queue_size=10)
    
    # change the intrinsics
    self.Cx = 650.407
    self.Cy = 357.483
    self.fx = 921.864
    self.fy = 922.567
    self.col = 1280
    self.row = 720
    self.hand_list = []
    self.cam_to_base_p = zeros(3)
    self.cam_to_base_q = zeros(4)
    self.frame_cam = "camera_top_color_optical_frame"
    self.bridge = CvBridge()
    self.blank_image = np.zeros((self.row,self.col,3), np.uint8)
    self.cv_image2 = np.zeros((self.row,self.col,3), np.uint8)
#===============================================================================================
# members
  def callback_hand(self, data):
    hand_t = data.header.stamp.to_sec()
    handedness = data.handedness.data
    wrist = [data.wrist.x, data.wrist.y, data.wrist.z]
    thumb_tip = [data.thumb_tip.x, data.thumb_tip.y, data.thumb_tip.z]
    index_tip = [data.index_tip.x, data.index_tip.y, data.index_tip.z]
    middle_tip = [data.middle_tip.x, data.middle_tip.y, data.middle_tip.z]
    ring_tip = [data.ring_tip.x, data.ring_tip.y, data.ring_tip.z]
    pinky_tip = [data.pinky_tip.x, data.pinky_tip.y, data.pinky_tip.z]
    index_mcp = [data.index_mcp.x, data.index_mcp.y, data.index_mcp.z]
    middle_mcp = [data.middle_mcp.x, data.middle_mcp.y, data.middle_mcp.z]
    ring_mcp = [data.ring_mcp.x, data.ring_mcp.y, data.ring_mcp.z]
    pinky_mcp = [data.pinky_mcp.x, data.pinky_mcp.y, data.pinky_mcp.z]
    
    palm = [wrist, index_mcp, middle_mcp, ring_mcp, pinky_mcp]
    hand_axy = mean(array(palm), axis=0)
    
    self.hand_list = [wrist, thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip, index_mcp, middle_mcp, ring_mcp, pinky_mcp, hand_axy]
    print('hand_3d_cam.py is running')
    print(handedness)

    
  def callback_image2(self, data):
    self.cv_image2 = self.bridge.imgmsg_to_cv2(data, "passthrough")
    cv_image2 = self.cv_image2
    scale = 1000.0
    
    hand_pc = []
    hand_list = self.hand_list
    r = 0
    g = 0
    b = 0
    a = 255
    rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
    
    for uv in hand_list:
      i = int(uv[1])
      j = int(uv[0]) 
      if i >= self.row:
        i =  self.row-1 
      elif i < 0:
        i = 0
      elif j >= self.col:
        j = self.col-1 
      elif j < 0:
        j = 0

      d = cv_image2[i][j]
      pt = [(float(j)-self.Cx)*d/self.fx/scale, (float(i)-self.Cy)*d/self.fy/scale, float(d)/scale, rgb]
      hand_pc.append(pt)

    HEADER = Header()
    HEADER.frame_id = self.frame_cam
    FIELDS = [
      PointField('x', 0, PointField.FLOAT32, 1),
      PointField('y', 4, PointField.FLOAT32, 1),
      PointField('z', 8, PointField.FLOAT32, 1),
      PointField('rgb', 12, PointField.UINT32, 1),
    ]
    POINTS = hand_pc#list
    outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
    self.hand_pc_pub.publish(outputPoints) 
    
  def callback_rgb(self, data):
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    # downsampled pc
    step = 10
    scale = 1000.0
    Cx = self.Cx
    Cy = self.Cy
    fx = self.fx
    fy = self.fy
    depth_img = []
    for i in range(0,self.row,step):
      for j in range(0,self.col,step):
        d = self.cv_image2[i][j]
        r = int(self.blank_image[i,j][0])
        g = int(self.blank_image[i,j][1])
        b = int(self.blank_image[i,j][2])
        a = 255
        rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
        pt = [(float(j)-Cx)*d/fx/scale,(float(i)-Cy)*d/fy/scale,float(d)/scale,rgb]
        depth_img.append(pt)
    HEADER = Header()
    HEADER.frame_id = 'camera_top_color_optical_frame'
    FIELDS = [
      PointField('x', 0, PointField.FLOAT32, 1),
      PointField('y', 4, PointField.FLOAT32, 1),
      PointField('z', 8, PointField.FLOAT32, 1),
      PointField('rgb', 12, PointField.UINT32, 1),
    ]
    POINTS = depth_img#list
    outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
    self.img_pc_pub.publish(outputPoints) 
    
def main(args):
  rospy.init_node('hand_3d_cam', anonymous=True)

  hd = hand_detect()

  
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

  main(sys.argv)
    
    
