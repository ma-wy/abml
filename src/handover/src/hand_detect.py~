#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

from handover.msg import hand_mp

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.bridge = CvBridge()
    self.rgb_sub = message_filters.Subscriber('/camera_top/color/image_raw', Image)
    self.rgb_sub.registerCallback(self.callback_rgb) 
#=======output==================================================================================
    self.hand_track_pub = rospy.Publisher("/hand_track",Image,queue_size=10)
    self.hand_msg_pub = rospy.Publisher("/hand_msg",hand_mp,queue_size=1)
#===============================================================================================
# members
    self.blank_image = np.zeros((720,1280,3), np.uint8)
    self.hand = np.zeros((720,1280,3), np.uint8)
    self.interest_area = np.zeros((720,1280,3), np.uint8)
    self.mp_drawing = mp.solutions.drawing_utils
    self.mp_drawing_styles = mp.solutions.drawing_styles
    self.mp_hands = mp.solutions.hands
    self.hand_list = hand_mp()
    self.hand_list.header.frame_id = "base"
    self.hand_list.header.stamp = rospy.Time.now() 

  def callback_rgb(self, data):
    self.hand_list.header.stamp = rospy.Time.now() 
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
          print(results.multi_handedness[0].classification[0].label)
          if results.multi_handedness[0].classification[0].label == 'Left':
            self.hand_list.handedness.data = 'right'
          elif results.multi_handedness[0].classification[0].label == 'Right':
            self.hand_list.handedness.data = 'left'
          for hand_landmarks in results.multi_hand_landmarks:
            self.hand_list.header.stamp = rospy.Time.now() 
            wrist_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].z]
            self.hand_list.wrist = give_Point(wrist_temp)
            thumb_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].z]
            self.hand_list.thumb_tip = give_Point(thumb_temp)
            index_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].z]
            self.hand_list.index_tip = give_Point(index_temp)
            middle_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z]
            self.hand_list.middle_tip = give_Point(middle_temp)
            ring_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].z]
            self.hand_list.ring_tip = give_Point(ring_temp)
            pinky_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].z]
            self.hand_list.pinky_tip = give_Point(pinky_temp)
            
            index_mcp_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].z]
            self.hand_list.index_mcp = give_Point(index_mcp_temp)
            middle_mcp_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z]
            self.hand_list.middle_mcp = give_Point(middle_mcp_temp)
            ring_mcp_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].z]
            self.hand_list.ring_mcp = give_Point(ring_mcp_temp)
            pinky_mcp_temp = [
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x * image_width), 
              int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * image_height),
              hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].z]
            self.hand_list.pinky_mcp = give_Point(pinky_mcp_temp)
            
            self.mp_drawing.draw_landmarks( # no difference with time of drawing or not 
              image,
              hand_landmarks,
              self.mp_hands.HAND_CONNECTIONS,
              self.mp_drawing_styles.get_default_hand_landmarks_style(),
              self.mp_drawing_styles.get_default_hand_connections_style())
            
    # Flip the image horizontally for a selfie-view display.
        self.hand = image
#        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        self.hand_msg_pub.publish(self.hand_list)
        self.hand_track_pub.publish(self.bridge.cv2_to_imgmsg(self.hand, "passthrough"))
    mark2 = time.time()
    print((mark2-mark1)*1000.0)
    
def main(args):
  rospy.init_node('hand_detect', anonymous=True)

  hd = hand_detect()
  
  while not rospy.is_shutdown():
    cv2.imshow("hand_detect", hd.hand)    
    if cv2.waitKey(1) == ord('q'):
      break
  cv2.destroyAllWindows()    
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
if __name__ == '__main__':

    main(sys.argv)
    
    
