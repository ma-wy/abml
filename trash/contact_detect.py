#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/kyle/Documents/maws/lib")
from mwy_path_python3 import *
from mwy_lib_python3 import *

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.bridge = CvBridge()
    self.gray_sub = rospy.Subscriber('/interestarea_1', Image, self.callback_image1)
    self.hand_track_sub = rospy.Subscriber("/hand_track",Image,self.callback_hand)
#=======output==================================================================================
#    self.hand_track_pub = rospy.Publisher("/hand_track",Image,queue_size=10)
#===============================================================================================
# members
    self.blank_image = np.zeros((720,1280,3), np.uint8)
    self.gray = np.zeros((720,1280,3), np.uint8)
    self.interest_area = np.zeros((720,1280,3), np.uint8)
    self.mp_drawing = mp.solutions.drawing_utils
    self.mp_drawing_styles = mp.solutions.drawing_styles
    self.mp_hands = mp.solutions.hands

  def callback_hand(self,data):
    self.interest_area = self.bridge.imgmsg_to_cv2(data, "passthrough")
    
  def callback_rgb(self, data):
    mark1 = time.time()
    image_width = 1280
    image_height = 720
    print()
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    with self.mp_hands.Hands(
      model_complexity=0,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
        image = self.blank_image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
    # Draw the hand annotations on the image.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
            finger_tip_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
            finger_tip_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
            radius = 10
            for i in range(finger_tip_x-radius, finger_tip_x+radius):
              for j in range(finger_tip_y-radius, finger_tip_y+radius):
                if self.interest_area[i,j]==255:
                  print("hand touches the object")
                  break
            self.mp_drawing.draw_landmarks(
              image,
              hand_landmarks,
              self.mp_hands.HAND_CONNECTIONS,
              self.mp_drawing_styles.get_default_hand_landmarks_style(),
              self.mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
        self.gray = image
#        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        
        self.hand_track_pub.publish(self.bridge.cv2_to_imgmsg(self.gray, "passthrough"))
    mark2 = time.time()
    print((mark2-mark1)*1000.0)
    
def main(args):
  rospy.init_node('hand_detect', anonymous=True)

#  cv2.namedWindow('raw_image')
#  cv2.namedWindow('gray_image')

  hd = hand_detect()

  while True:
#    cv2.imshow("raw_image", hd.interest_area)
#    cv2.imshow("gray_image", hd.gray)    
    if cv2.waitKey(1) == ord('q'):
      break
  cv2.destroyAllWindows()
  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
