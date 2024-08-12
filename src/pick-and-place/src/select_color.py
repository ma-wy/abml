#!/usr/bin/env python2.7
import sys 
sys.path.append("/home/mawanyu/MAws/lib")
from mwy_lib import *
from mwy_path import *

class select_color:
  def __init__(self):
#=======input==================================================================================
    self.bridge = CvBridge()
    self.rgb_sub = message_filters.Subscriber('/camera1/color/image_raw', Image)
    self.rgb_sub.registerCallback(self.callback_rgb) 
#=======output==================================================================================
    self.interest_area_pub = rospy.Publisher("/interestarea_1",Image,queue_size=10)
#===============================================================================================
# members
    self.blank_image = np.zeros((720,1280,3), np.uint8)
    self.gray = np.zeros((720,1280,3), np.uint8)
    self.line = np.zeros((720,1280,3), np.uint8)
    self.hsv = np.zeros((720,1280,3), np.uint8)
    self.ix = 0
    self.iy = 0
    self.CHOOSE_COLOR = False
    self.TRACK_COLOR = False
    self.track_h = 0
    self.track_s = 0
    self.track_v = 0
    self.row = 720
    self.col = 1280

  def on_mouse(self,event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
      self.ix,self.iy = x,y
      self.CHOOSE_COLOR = True

  def callback_rgb(self, data):
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    colNum = data.width
    rowNum = data.height
    cv2.setMouseCallback('raw_image', self.on_mouse)
    thd_h = cv2.getTrackbarPos("thd_h", "raw_image")
    thd_s = cv2.getTrackbarPos("thd_s", "raw_image")
    thd_v = cv2.getTrackbarPos("thd_v", "raw_image")
    self.hsv = cv2.cvtColor(self.blank_image, cv2.COLOR_BGR2HSV)
#    self.gray = cv2.cvtColor(self.blank_image, cv2.COLOR_BGR2GRAY)
    if self.CHOOSE_COLOR == True:
      self.track_h = self.hsv[self.iy,self.ix][0]
      self.track_s = self.hsv[self.iy,self.ix][1]
      self.track_v = self.hsv[self.iy,self.ix][2] 
      print "HSV: " + str(self.track_h) + ", " + str(self.track_s) + ", " + str(self.track_v)  
      self.CHOOSE_COLOR = False
      self.TRACK_COLOR = True
    if self.TRACK_COLOR == True:
      gray = cv2.inRange(self.hsv, (self.track_h-thd_h, self.track_s-thd_s, self.track_v-thd_v), (self.track_h+thd_h, self.track_s+thd_s, self.track_v+thd_v))    
      ed1 = cv2.getTrackbarPos("edparam1", "raw_image")
      ed2 = cv2.getTrackbarPos("edparam2", "raw_image")
      ed3 = cv2.getTrackbarPos("edparam3", "raw_image")
      ed0 = cv2.getTrackbarPos("edparam0", "raw_image")
      kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ed1, ed1))
      kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ed2, ed2))
      kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ed3, ed3))
      kernel0 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ed0, ed0))
      for i in range(2):
        gray = cv2.dilate(gray, kernel0)
        gray = cv2.erode(gray, kernel0)
      for i in range(2):
        gray = cv2.dilate(gray, kernel1)
      for i in range(2):
        gray = cv2.erode(gray, kernel2)
      self.gray = gray
    self.interest_area_pub.publish(self.bridge.cv2_to_imgmsg(self.gray, "passthrough"))
# class end=========================================================================================

def image_processing_h(thd_h):
  pass
def image_processing_s(thd_s):
  pass
def image_processing_v(thd_v):
  pass
def image_processing_ed0(edparam0):
  pass
def image_processing_ed1(edparam1):
  pass
def image_processing_ed2(edparam2):
  pass
def image_processing_ed3(edparam3):
  pass

def main(args):
  rospy.init_node('select_color', anonymous=True)

  cv2.namedWindow('raw_image')
#  cv2.namedWindow('gray_image')

  cv2.createTrackbar( "thd_h", "raw_image", 0, 30, image_processing_h )
  cv2.createTrackbar( "thd_s", "raw_image", 0, 30, image_processing_s )
  cv2.createTrackbar( "thd_v", "raw_image", 0, 30, image_processing_v )
  cv2.createTrackbar( "edparam0", "raw_image", 0, 30, image_processing_ed0 )
  cv2.createTrackbar( "edparam1", "raw_image", 0, 30, image_processing_ed1 )
  cv2.createTrackbar( "edparam2", "raw_image", 0, 40, image_processing_ed2 )
  cv2.createTrackbar( "edparam3", "raw_image", 0, 20, image_processing_ed3)
  cv2.setTrackbarPos("thd_h", "raw_image", 5) # green foam: 15  pink foam:5
  cv2.setTrackbarPos("thd_s", "raw_image", 25)
  cv2.setTrackbarPos("thd_v", "raw_image", 30)
  cv2.setTrackbarPos("edparam0", "raw_image", 20) #
  cv2.setTrackbarPos("edparam1", "raw_image", 20) #
  cv2.setTrackbarPos("edparam2", "raw_image", 23) #
  cv2.setTrackbarPos("edparam3", "raw_image", 1)
  sc = select_color()

  while True:
    cv2.imshow("raw_image", sc.blank_image)    
#    cv2.imshow("gray_image", sc.gray)
    if cv2.waitKey(1) == ord('q'):
      break
  cv2.destroyAllWindows()
  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)

