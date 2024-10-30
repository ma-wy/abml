#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

class generate_target():
  def __init__(self):
#input==============================================================================================  
    self.grasping_point_sub = rospy.Subscriber("/grasping_point", Point32, self.callback_grasping_point)
    self.handle_point_sub = rospy.Subscriber("/handle_point", Point32, self.callback_handle_point)
    self.ee_in_ee3_tf_sub = rospy.Subscriber("/ee_in_ee3_tf", Pose, self.callback_ee_in_ee3)
    self.cam_in_base_tf_sub = rospy.Subscriber("/cam_in_base_tf", Pose, self.callback_cam_in_base)
#output=======================================================================================      
    self.ee_goal_in_base_pub = rospy.Publisher("/ee_target_in_base", PoseStamped, queue_size=1)   
    self.ee3_goal_in_base_pub = rospy.Publisher("/ee3_target_in_base", PoseStamped, queue_size=1)
    #self.grasping_point_pub = rospy.Publisher("/grasping", PointStamped, queue_size=1)
    #self.handle_point_pub = rospy.Publisher("/handle", PointStamped, queue_size=1)
    
#member===========================================================================================      
    self.grasping_point = zeros(3)
    self.handle_point = zeros(3)

    self.rob = MoveGroupCommander('panda_arm')
    self.rob.set_end_effector_link('panda_hand_tcp')
    #os.system("rosrun franka_basic_motion grasping_init.py grasping")
    self.ee_in_ee3_tf = []
    self.cam_in_base_tf = []
    self.bias = array([0, 0, -0.017])
    self.if_recieved_handle = False
    self.if_recieved_grasping = False
    
  def callback_ee_in_ee3(self, data):
    self.ee_in_ee3_tf = get_Pose(data)
    #print('self.ee_in_ee3_tf')
    #print(self.ee_in_ee3_tf)
    
  def callback_cam_in_base(self, data):
    self.cam_in_base_tf = get_Pose(data)
    #print('self.cam_in_base_tf')
    #print(self.cam_in_base_tf)
    
  def callback_handle_point(self, data):
    handle_point_cam = array(get_Point(data))   
    self.handle_point = transformation_P(handle_point_cam, self.cam_in_base_tf[:3], self.cam_in_base_tf[3:]) + self.bias
    self.if_recieved_handle = True
    print('handle')
    print(self.handle_point)
    
  def callback_grasping_point(self, data):
    grasping_point_cam = array(get_Point(data))
    self.grasping_point = transformation_P(grasping_point_cam, self.cam_in_base_tf[:3], self.cam_in_base_tf[3:]) + self.bias
    self.if_recieved_grasping = True
    print('grasping')
    print(self.grasping_point)
    print()
    print(self.if_recieved_handle)
    print(self.if_recieved_grasping)
    if self.if_recieved_handle == True and self.if_recieved_grasping == True:
      # align x axis with the instrument
      x_axis_new = (self.handle_point - self.grasping_point)/norm(self.handle_point - self.grasping_point)
      posestamped_crr = self.rob.get_current_pose()
      pose_crr = get_PoseStamped(posestamped_crr)
      p_crr = pose_crr[:3]
      q_crr = pose_crr[3:]
      T = tf.transformations.quaternion_matrix(q_crr).T
      x_axis_old = T[0,0:3]
      q_rot = rotation_between_2v(x_axis_old, x_axis_new)
      q_new = transformation_Q(q_crr, q_rot)  
      # ee3 target
      ee3_target_pose = give_PoseStamped(posestamped_crr.header.frame_id, q_new, self.grasping_point)
      self.ee3_goal_in_base_pub.publish(ee3_target_pose)
      # ee target
      # trans the target position of the third finger to the ee's
      p_new = transformation_P(self.ee_in_ee3_tf[:3], self.grasping_point, q_new)
      ee_target_pose = give_PoseStamped(posestamped_crr.header.frame_id, q_new, p_new)
      print(ee_target_pose)
      self.ee_goal_in_base_pub.publish(ee_target_pose)
      self.if_recieved_handle = False
      self.if_recieved_grasping = False
    
    




def main(args):
  rospy.init_node("generate_target", anonymous=True)
  gt = generate_target()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
    
    

