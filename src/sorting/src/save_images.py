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
#=======output==================================================================================
#===============================================================================================
# members
    self.bridge = CvBridge()
    self.row = 480
    self.col = 640
    self.blank_image = np.zeros((self.row,self.col,3), np.uint8)
    
  def callback_rgb(self, data):
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    
# class end=========================================================================================


def main(args):
  
  rospy.init_node('save_image', anonymous=True)
  gp = grasping_point()
  
  num = '4'
  save_path = os.path.join('/home/abml/zoe_data/sorting/', num)
  check_make_clear_folder(save_path)
  while not rospy.is_shutdown():
    time.sleep(0.033)
    cv2.imshow("raw_image", gp.blank_image)    
    if cv2.waitKey(1) == ord('q'):
      break  
    cv2.imwrite(os.path.join(save_path, name_time()+ '.jpg'), gp.blank_image)
  cv2.destroyAllWindows()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)





