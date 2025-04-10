#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

from handover.msg import hand_mp

class hand_detect:
  def __init__(self):
#=======input==================================================================================
    self.bridge = CvBridge()
    self.rgb_sub = message_filters.Subscriber('/camera/color/image_raw', Image)
    self.rgb_sub.registerCallback(self.callback_rgb) 
    self.image2_sub = message_filters.Subscriber('/camera/aligned_depth_to_color/image_raw', Image)#, queue_size=2
    self.image2_sub.registerCallback(self.callback_depth)     
#=======output==================================================================================
    self.hand_track_pub = rospy.Publisher("/hand_track", Image, queue_size=1)
    self.hand_msg_pub = rospy.Publisher("/hand_msg", hand_mp, queue_size=1)
    self.if_hand_pub = rospy.Publisher("/if_hand", Bool, queue_size=1)
    
    self.wrist_pub = rospy.Publisher("/wrist",PointStamped,queue_size=1)
    self.thumb_1_pub = rospy.Publisher("/thumb_1",PointStamped,queue_size=1)
    self.thumb_2_pub = rospy.Publisher("/thumb_2",PointStamped,queue_size=1)
    self.thumb_3_pub = rospy.Publisher("/thumb_3",PointStamped,queue_size=1)
    self.thumb_4_pub = rospy.Publisher("/thumb_4",PointStamped,queue_size=1)
    self.index_1_pub = rospy.Publisher("/index_1",PointStamped,queue_size=1)
    self.index_2_pub = rospy.Publisher("/index_2",PointStamped,queue_size=1)
    self.index_3_pub = rospy.Publisher("/index_3",PointStamped,queue_size=1)
    self.index_4_pub = rospy.Publisher("/index_4",PointStamped,queue_size=1)
    self.middle_1_pub = rospy.Publisher("/middle_1",PointStamped,queue_size=1)
    self.middle_2_pub = rospy.Publisher("/middle_2",PointStamped,queue_size=1)
    self.middle_3_pub = rospy.Publisher("/middle_3",PointStamped,queue_size=1)
    self.middle_4_pub = rospy.Publisher("/middle_4",PointStamped,queue_size=1)
    self.ring_1_pub = rospy.Publisher("/ring_1",PointStamped,queue_size=1)
    self.ring_2_pub = rospy.Publisher("/ring_2",PointStamped,queue_size=1)
    self.ring_3_pub = rospy.Publisher("/ring_3",PointStamped,queue_size=1)
    self.ring_4_pub = rospy.Publisher("/ring_4",PointStamped,queue_size=1)
    self.pinky_1_pub = rospy.Publisher("/pinky_1",PointStamped,queue_size=1)
    self.pinky_2_pub = rospy.Publisher("/pinky_2",PointStamped,queue_size=1)
    self.pinky_3_pub = rospy.Publisher("/pinky_3",PointStamped,queue_size=1)
    self.pinky_4_pub = rospy.Publisher("/pinky_4",PointStamped,queue_size=1)
    '''
    self.palm_pub = rospy.Publisher("/palm_points",PointCloud2,queue_size=1)
    self.thumb_pub = rospy.Publisher("/thumb_points",PointCloud2,queue_size=1)
    self.index_pub = rospy.Publisher("/index_points",PointCloud2,queue_size=1)
    self.middle_pub = rospy.Publisher("/middle_points",PointCloud2,queue_size=1)
    self.ring_pub = rospy.Publisher("/ring_points",PointCloud2,queue_size=1)
    self.pinky_pub = rospy.Publisher("/pinky_points",PointCloud2,queue_size=1)
    '''
#===============================================================================================
# members
    self.row = 480
    self.col = 640
    self.blank_image = np.zeros((self.row,self.col,3), np.uint8)
    self.depth = np.zeros((self.row,self.col,3), np.uint8)
    self.hand = np.zeros((self.row,self.col,3), np.uint8)
    self.interest_area = np.zeros((self.row,self.col,3), np.uint8)
    self.mp_drawing = mp.solutions.drawing_utils
    self.mp_drawing_styles = mp.solutions.drawing_styles
    self.mp_hands = mp.solutions.hands
    self.hand_list = hand_mp()
    self.hand_list.header.frame_id = "base"
    self.hand_list.header.stamp = rospy.Time.now() 
    self.hand_list_pre = self.hand_list
    self.if_hand = Bool()
    self.if_hand.data = False
    self.hand_p_name = ['WRIST', 'THUMB_CMC', 'THUMB_MCP', 'THUMB_IP', 'THUMB_TIP', 'INDEX_FINGER_MCP', 'INDEX_FINGER_PIP', 'INDEX_FINGER_DIP', 'INDEX_FINGER_TIP', 'MIDDLE_FINGER_MCP', 'MIDDLE_FINGER_PIP', 'MIDDLE_FINGER_DIP', 'MIDDLE_FINGER_TIP', 'RING_FINGER_MCP', 'RING_FINGER_PIP', 'RING_FINGER_DIP', 'RING_FINGER_TIP', 'PINKY_MCP', 'PINKY_PIP', 'PINKY_DIP', 'PINKY_TIP'] 
    self.frame = 'camera_color_optical_frame'
    self.hand_p_dict = {}
    self.hand_p_pub_list = [self.wrist_pub, self.thumb_1_pub, self.thumb_2_pub, self.thumb_3_pub, self.thumb_4_pub, self.index_1_pub, self.index_2_pub, self.index_3_pub, self.index_4_pub, self.middle_1_pub, self.middle_2_pub, self.middle_3_pub, self.middle_4_pub, self.ring_1_pub, self.ring_2_pub, self.ring_3_pub, self.ring_4_pub, self.pinky_1_pub, self.pinky_2_pub, self.pinky_3_pub, self.pinky_4_pub]
    print('ready to detect hand')
    
    
  def callback_depth(self,data):
    self.depth = self.bridge.imgmsg_to_cv2(data, "passthrough")
        
        
  def callback_rgb(self, data):
    self.hand_list.header.stamp = rospy.Time.now() 
    mark1 = time.time()
    image_width = self.col
    image_height = self.row
    print()
    print('hand_detect.py is running')
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    Cx, Cy, fx, fy = realsense_intrinsics('d435', self.row, self.col)
    with self.mp_hands.Hands(
      model_complexity=0,
      min_detection_confidence=0.4,
      min_tracking_confidence=0.4) as hands:
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
        image = self.blank_image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
    # Draw the hand annotations on the image.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
     # if there is a hand, pub if_hand
        if results.multi_hand_landmarks:
          self.if_hand.data = True
          print("#############")
          print("hand detected")
          print("#############")
          for hand_landmarks in results.multi_hand_landmarks:
            self.hand_list.header.stamp = rospy.Time.now() 
            # 0
            x0 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x * image_width)
            y0 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].y * image_height)
            z0 = self.depth[y0][x0]
            p0 = generate_pt([x0,y0,z0], Cx, Cy, fx, fy)
            wrist = give_PointStamped(self.frame, p0) 

            # 1
            x1 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].x * image_width)
            y1 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].y * image_height)
            z1 = self.depth[y1][x1]
            p1 = generate_pt([x1,y1,z1], Cx, Cy, fx, fy)
            thumb_1 = give_PointStamped(self.frame, p1)   
            
            # 2
            x2 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * image_width)
            y2 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * image_height)
            z2 = self.depth[y2][x2]
            p2 = generate_pt([x2,y2,z2], Cx, Cy, fx, fy)
            thumb_2 = give_PointStamped(self.frame, p2)
            
            # 3
            x3 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].x * image_width)
            y3 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].y * image_height)
            z3 = self.depth[y3][x3]
            p3 = generate_pt([x3,y3,z3], Cx, Cy, fx, fy)
            thumb_3 = give_PointStamped(self.frame, p3)           
            
            # 4 
            x4 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * image_width)
            y4 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * image_height)
            z4 = self.depth[y4][x4]
            p4 = generate_pt([x4,y4,z4], Cx, Cy, fx, fy)
            thumb_4 = give_PointStamped(self.frame, p4)    
            
            # 5
            x5 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width)
            y5 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height)
            z5 = self.depth[y5][x5]
            p5 = generate_pt([x5,y5,z5], Cx, Cy, fx, fy)
            index_1 = give_PointStamped(self.frame, p5)    
            
            # 6
            x6 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width)
            y6 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height)
            z6 = self.depth[y6][x6]
            p6 = generate_pt([x6,y6,z6], Cx, Cy, fx, fy)
            index_2 = give_PointStamped(self.frame, p6)    
            
            # 7
            x7 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width)
            y7 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height)
            z7 = self.depth[y7][x7]
            p7 = generate_pt([x7,y7,z7], Cx, Cy, fx, fy)
            index_3 = give_PointStamped(self.frame, p7)    
            
            # 8
            x8 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
            y8 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
            z8 = self.depth[y8][x8]
            p8 = generate_pt([x8,y8,z8], Cx, Cy, fx, fy)
            index_4 = give_PointStamped(self.frame, p8)     
            
            # 9
            x9 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width)
            y9 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height)
            z9 = self.depth[y9][x9]
            p9 = generate_pt([x9,y9,z9], Cx, Cy, fx, fy)
            middle_1 = give_PointStamped(self.frame, p9)  
            
            # 10
            x10 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width)
            y10 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height)
            z10 = self.depth[y10][x10]
            p10 = generate_pt([x10,y10,z10], Cx, Cy, fx, fy)
            middle_2 = give_PointStamped(self.frame, p10)  
            
            # 11
            x11 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width)
            y11 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height)
            z11 = self.depth[y11][x11]
            p11 = generate_pt([x11,y11,z11], Cx, Cy, fx, fy)
            middle_3 = give_PointStamped(self.frame, p11)  
            
            # 12
            x12 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width)
            y12 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height)
            z12 = self.depth[y12][x12]
            p12 = generate_pt([x12,y12,z12], Cx, Cy, fx, fy)
            middle_4 = give_PointStamped(self.frame, p12) 
            
            # 13
            x13 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width)
            y13 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height)
            z13 = self.depth[y13][x13]
            p13 = generate_pt([x13,y13,z13], Cx, Cy, fx, fy)
            ring_1 = give_PointStamped(self.frame, p13) 
            
            # 14
            x14 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width)
            y14 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height)
            z14 = self.depth[y14][x14]
            p14 = generate_pt([x14,y14,z14], Cx, Cy, fx, fy)
            ring_2 = give_PointStamped(self.frame, p14) 
            
            # 15
            x15 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width)
            y15 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height)
            z15 = self.depth[y15][x15]
            p15 = generate_pt([x15,y15,z15], Cx, Cy, fx, fy)
            ring_3 = give_PointStamped(self.frame, p15) 
            
            # 16
            x16 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width)
            y16 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height)
            z16 = self.depth[y16][x16]
            p16 = generate_pt([x16,y16,z16], Cx, Cy, fx, fy)
            ring_4 = give_PointStamped(self.frame, p16) 
            
            # 17
            x17 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x * image_width)
            y17 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * image_height)
            z17 = self.depth[y17][x17]
            p17 = generate_pt([x17,y17,z17], Cx, Cy, fx, fy)
            pinky_1 = give_PointStamped(self.frame, p17) 
            
            # 18
            x18 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].x * image_width)
            y18 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * image_height)
            z18 = self.depth[y18][x18]
            p18 = generate_pt([x18,y18,z18], Cx, Cy, fx, fy)
            pinky_2 = give_PointStamped(self.frame, p18) 
            
            # 19
            x19 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].x * image_width)
            y19 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].y * image_height)
            z19 = self.depth[y19][x19]
            p19 = generate_pt([x19,y19,z19], Cx, Cy, fx, fy)
            pinky_3 = give_PointStamped(self.frame, p19) 
            
            # 20
            x20 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * image_width)
            y20 = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * image_height)
            z20 = self.depth[y20][x20]
            p20 = generate_pt([x20,y20,z20], Cx, Cy, fx, fy)
            pinky_4 = give_PointStamped(self.frame, p20) 
            
            
            hand_p_list = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
            hand_p_to_pub = [wrist, thumb_1, thumb_2, thumb_3, thumb_4, index_1, index_2, index_3, index_4, middle_1, middle_2, middle_3, middle_4, ring_1, ring_2, ring_3, ring_4, pinky_1, pinky_2, pinky_3, pinky_4]
#            hand_p_line = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20
#            saveDataStep(hand_p_line, '/home/abml/zoe_ws/src/handover/src/hand_p_21_temp.txt', if_clear = False)
            
            hand_mean = np.mean(hand_p_list, axis=0)
            hand_std = std(hand_p_list, axis=0)
            threshold = 1.5
            for i in range(21):
              print()
              print([abs(hand_p_list[i][j] - hand_mean[j]) for j in range(3)])
              print([threshold * hand_std[j] for j in range(3)])
              if all([abs(hand_p_list[i][j] - hand_mean[j]) < threshold * hand_std[j] for j in range(3)]):
                self.hand_p_pub_list[i].publish(hand_p_to_pub[i])
                
        
            
            
            '''
            self.wrist_pub.publish(wrist)
            self.thumb_1_pub.publish(thumb_1)
            self.thumb_2_pub.publish(thumb_2)
            self.thumb_3_pub.publish(thumb_3)
            self.thumb_4_pub.publish(thumb_4)
            self.index_1_pub.publish(index_1)
            self.index_2_pub.publish(index_2)
            self.index_3_pub.publish(index_3)
            self.index_4_pub.publish(index_4)
            self.middle_1_pub.publish(middle_1)
            self.middle_2_pub.publish(middle_2)
            self.middle_3_pub.publish(middle_3)
            self.middle_4_pub.publish(middle_4)
            self.ring_1_pub.publish(ring_1)
            self.ring_2_pub.publish(ring_2)
            self.ring_3_pub.publish(ring_3)
            self.ring_4_pub.publish(ring_4)
            self.pinky_1_pub.publish(pinky_1)
            self.pinky_2_pub.publish(pinky_2)
            self.pinky_3_pub.publish(pinky_3)
            self.pinky_4_pub.publish(pinky_4)
            '''
            
            
            self.mp_drawing.draw_landmarks( # no difference with time of drawing or not 
              image,
              hand_landmarks,
              self.mp_hands.HAND_CONNECTIONS,
              self.mp_drawing_styles.get_default_hand_landmarks_style(),
              self.mp_drawing_styles.get_default_hand_connections_style())
            
            
        else:
          print("****************")
          print("no hand detected")
          print("****************")
 
        
        mark2 = time.time()
        print((mark2-mark1)*1000.0)
            
    # Flip the image horizontally for a selfie-view display.
        self.hand = image
#        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        self.hand_msg_pub.publish(self.hand_list)
        self.hand_track_pub.publish(self.bridge.cv2_to_imgmsg(self.hand, "passthrough"))
        self.if_hand_pub.publish(self.if_hand)
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
    
    
