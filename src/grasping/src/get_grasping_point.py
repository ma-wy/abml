#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *



class grasping_point:
  def __init__(self):
#=======input==================================================================================
    self.rgb_sub = message_filters.Subscriber('/camera/color/image_raw', Image)
    self.rgb_sub.registerCallback(self.callback_rgb) 
    self.depth_sub = message_filters.Subscriber('/camera/aligned_depth_to_color/image_raw', Image) #, queue_size=2
    self.depth_sub.registerCallback(self.callback_depth) 
#=======output==================================================================================
    self.grasping_point_pub = rospy.Publisher("/grasping_point", Point32, queue_size=1)
    self.handle_point_pub = rospy.Publisher("/handle_point", Point32, queue_size=1)
#===============================================================================================
# members
#311.867 254.023 
#369.615 552.456 460.460 520.072 336.453 172.203 245.607 204.587
    
    self.row = 480
    self.col = 640
    self.blank_image = np.zeros((self.row,self.col,3), np.uint8)
    self.depth_image = np.zeros((self.row,self.col,3), np.uint8)
    self.Cx = 317.494
    self.Cy = 246.239
    self.fx = 607.652
    self.fy = 607.507
    
    ####################
    self.bridge = CvBridge()
    
    self.if_compute_depth = False
    self.choose_grasping_point = False
    self.choose_handle_point = False
    self.count = 0
    self.grasping_pix = [0,0]
    self.handle_pix = [0,0]
    self.grasping_point = give_Point(zeros(3))
    self.handle_point = give_Point(zeros(3))
    
    
  def on_mouse(self,event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
      self.grasping_pix = [int(x),int(y)]
      self.choose_grasping_point = True    
      scale = 1000.0
      x = self.grasping_pix[0]
      y = self.grasping_pix[1]
      d = self.depth_image[int(y)][int(x)]
      p =[(x-self.Cx)*d/self.fx/scale,(y-self.Cy)*d/self.fy/scale,float(d)/scale]   
      self.grasping_point = give_Point(p) 
      
    if event == cv2.EVENT_MBUTTONDOWN:
      self.handle_pix = [int(x),int(y)]
      self.choose_handle_point = True   
      scale = 1000.0
      x = self.handle_pix[0]
      y = self.handle_pix[1]
      d = self.depth_image[int(y)][int(x)]
      p = [(x-self.Cx)*d/self.fx/scale,(y-self.Cy)*d/self.fy/scale,float(d)/scale]      
      self.handle_point = give_Point(p) 
      
  ##############################  
  def callback_depth(self, data):  
    self.depth_image = self.bridge.imgmsg_to_cv2(data, "passthrough")
    
  def callback_rgb(self, data):
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.setMouseCallback('raw_image', self.on_mouse)
    
    self.blank_image = cv2.circle(self.blank_image, self.grasping_pix, 3, (0,0,255), 2)   
    self.blank_image = cv2.circle(self.blank_image, self.handle_pix, 3, (0,255,0), 2) 
    self.grasping_point_pub.publish(self.grasping_point) 
    self.handle_point_pub.publish(self.handle_point) 
# class end=========================================================================================


def main(args):
  
  rospy.init_node('grasping_point', anonymous=True)
  gp = grasping_point()

  while not rospy.is_shutdown():
    cv2.imshow("raw_image", gp.blank_image)    
    if cv2.waitKey(1) == ord('q'):
      break
  cv2.destroyAllWindows()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)





