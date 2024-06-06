#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from pose_transform_functions import  array_quat_2_pose, list_2_quaternion, position_2_array, transform_pose
from panda import Panda



class move_franka(Panda):
    def __init__(self):
      super(move_franka, self).__init__()
#input==============================================================================================      
      self.tool_poses_sub = rospy.Subscriber("/tool_poses",PoseArray,self.callback_tool_poses)
      self.cam_to_base_sub = rospy.Subscriber("/cam_to_base_tf",Pose,self.callback_cam_to_base_tf)
      self.ee_to_ee3_sub = rospy.Subscriber("/ee_to_ee3_tf",Pose,self.callback_ee_to_ee3_tf)
      self.set_goal_ee3_sub = rospy.Subscriber('/set_goal_ee3', Bool, self.callback_set_goal_ee3)
# rostopic pub /set_goal_ee3 std_msgs/Bool "data: False" 
# rostopic pub /set_goal_ee3 std_msgs/Bool "data: True" 
#output=======================================================================================      
      self.ee_goal_in_base_pub = rospy.Publisher("/ee_target_in_base",PoseStamped,queue_size=1)   
      self.ee3_goal_in_base_pub = rospy.Publisher("/ee3_target_in_base",PoseStamped,queue_size=1)
#member===========================================================================================      
      self.p_ee = zeros(3)
      self.q_ee = zeros(4)
      self.cam_to_base_p = zeros(3)
      self.cam_to_base_q = zeros(4)
      self.ee_to_ee3_p = zeros(3)
      self.ee_to_ee3_q = zeros(4)

    def callback_cam_to_base_tf(self, data):
      self.cam_to_base_p = [data.position.x, data.position.y, data.position.z]
      self.cam_to_base_q = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]

    def callback_ee_to_ee3_tf(self, data):
      self.ee_to_ee3_p = [data.position.x, data.position.y, data.position.z]
      self.ee_to_ee3_q = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]

    def callback_tool_poses(self, data):
      p_list = []
      q_list = []
      for pose in data.poses:
        p_list.append([pose.position.x, pose.position.y, pose.position.z])
        q_list.append([pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w])#xyzw

      p = p_list[0]
      q = q_list[0] #xyzw
      
      # ee3 target in camera frame
      # trans to ee3 target in base frame
      trans = array(self.cam_to_base_p)
      q_rot = array(self.cam_to_base_q) #xyzw
     
      v_old = p
      p_ee3 = transformation_P(v_old,trans,q_rot)
      
      q_orig = q
      q_ee3_xyzw = transformation_Q(q_orig,q_rot)
      q_ee3_wxyz = q_xyzw_to_wxyz(q_ee3_xyzw)  # return a list
      q_ee3 = list_2_quaternion(q_ee3_wxyz) # input q = [w, x, y, z]
      
      frame = "panda_link0"
      ee3_target_in_base = give_PoseStamped(frame, q_ee3_xyzw, p_ee3)
      self.ee3_goal_in_base_pub.publish(ee3_target_in_base)
      
      # trans to ee target in base frame
# base_T_ee = base_T_ee3 dot inv(ee_T_ee3)
# transformation = base_T_ee3 (taraget)
# origin = inv(ee_T_ee3) = ee3_T_ee
      trans = p_ee3
      q_rot = q_ee3_xyzw #xyzw
     
      v_old = array(self.ee_to_ee3_p)
      p_ee = transformation_P(v_old,trans,q_rot)

      q_orig = array(self.ee_to_ee3_q)
      q_ee_xyzw = transformation_Q(q_orig,q_rot)
      q_ee_wxyz = q_xyzw_to_wxyz(q_ee_xyzw)  # return a list
      q_ee = list_2_quaternion(q_ee_wxyz) # input q = [w, x, y, z]
      
      frame = "panda_link0"
      ee_target_in_base = give_PoseStamped(frame, q_ee_xyzw, p_ee)
      self.ee_goal_in_base_pub.publish(ee_target_in_base)      
      
      # for control
      self.p_ee = p_ee
      self.q_ee = q_ee


# rostopic pub /set_goal_ee3 std_msgs/Bool "data: False" 
# rostopic pub /set_goal_ee3 std_msgs/Bool "data: True" 
    def callback_set_goal_ee3(self, data):
      print(data)
      p_ee = self.p_ee
      p_ee[-1] = 0.0
      q_ee = self.q_ee
      goal_ee3_in_base = array_quat_2_pose(p_ee, q_ee)
      if data.data:
        print("move panda_EE to the goal")
        self.goal_pub.publish(goal_ee3_in_base)
      else:
        print("p_ee target")
        print(goal_ee3_in_base)

def main(args):
  rospy.init_node("move_franka", anonymous=True)
  mf = move_franka()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
    
    

