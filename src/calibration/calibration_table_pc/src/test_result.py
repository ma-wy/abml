#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *

class test_result:
  def __init__(self):
#=======input==================================================================================
    self.rgb_sub = message_filters.Subscriber('/camera/color/image_raw', Image)
    self.rgb_sub.registerCallback(self.callback_rgb) 
#=======output==================================================================================
    self.target_pub = rospy.Publisher("/test_polyfit_result", PoseStamped, queue_size=1)
#===============================================================================================
# members
    self.bridge = CvBridge()
    self.row = 480
    self.col = 640
    self.blank_image = np.zeros((self.row,self.col,3), np.uint8)
    self.ix = 0
    self.iy = 0
    self.CHOOSE_COLOR = False
    self.TRACK_PT = False
    self.count = 0
    
    self.rob = MoveGroupCommander('panda_arm')
    self.rob.set_end_effector_link('panda_hand_tcp')
    os.system("rosrun franka_basic_motion grasping_init.py grasping")
    
  def on_mouse(self,event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
      self.ix,self.iy = x,y
      self.CHOOSE_COLOR = True

  def callback_rgb(self, data):
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.setMouseCallback('raw_image', self.on_mouse)
    if self.CHOOSE_COLOR == True:
      self.count += 1
      #self.pt = polyfit_2d_to_3d([self.ix,self.iy])
      self.pt = bias_2d_to_3d([self.ix,self.iy])
      print([self.ix,self.iy])
      print(self.pt)
      #os.system("rosrun franka_basic_motion grasping_init.py grasping")
      #os.system("rosrun franka_basic_motion reset_gripper_ori.py")
      self.TRACK_PT = True
      self.CHOOSE_COLOR = False
    if self.count > 0:
      self.blank_image = cv2.circle(self.blank_image, [self.ix,self.iy], 3, (0,0,255), 2) 
      target = self.rob.get_current_pose()
      target.pose.position.x = self.pt[0]
      target.pose.position.y = self.pt[1]
      target.pose.position.z = -0.06
      print(target)
      self.target_pub.publish(target)
    if self.TRACK_PT == True:
      #self.rob.go(target)
      #os.system("rosrun franka_basic_motion trans_axis.py z -0.455")
      self.TRACK_PT = False
        
# class end=========================================================================================


def main(args):
  rospy.init_node('test_result', anonymous=True)
  cv2.namedWindow('raw_image')

  tr = test_result()

  while not rospy.is_shutdown():
    cv2.imshow("raw_image", tr.blank_image)    
    if cv2.waitKey(1) == ord('q'):
      break
  cv2.destroyAllWindows()
  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)



