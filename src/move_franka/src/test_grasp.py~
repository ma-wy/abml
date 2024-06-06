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
      self.ee_goal_in_base_sub = rospy.Subscriber("/ee_target_in_base",PoseStamped,self.callback_ee_goal_in_base)
#      self.set_goal_ee3_sub = rospy.Subscriber('/set_goal_ee3', Bool, self.callback_set_goal_ee3)
# rostopic pub /set_goal_ee3 std_msgs/Bool "data: False" 
# rostopic pub /set_goal_ee3 std_msgs/Bool "data: True" 
      self.set_goal_ee3_sub = rospy.Subscriber('/set_goal_ee3', Float64MultiArray, self.callback_set_goal_ee3)
# rostopic pub /set_goal_ee3 std_msgs/Float64MultiArray "data: [0.48, 0.0, 0.51, 0.707, -0.707, 0.0, 0.0]" 
      self.p_ee = zeros(3)
      self.q_ee = zeros(4)
      self.ee_target_p = array([0.5067963183582014, 0.010948362447869966, -0.05967133095095972])
      self.ee_target_q = array([0.9529543339979524, 0.30282280826228236, 0.012997946134995893, -0.0035923262735036293])
      #current q = [0.9919463499189227, -0.0009561534711263993, -0.1260761803175022, -0.011895718022736947]

    def callback_ee_goal_in_base(self, data):
      self.p_ee = [data.pose.position.x, data.pose.position.y, data.pose.position.z]
      self.q_ee = [data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z, data.pose.orientation.w]

# rostopic pub /set_goal_ee3 std_msgs/Bool "data: False" 
# rostopic pub /set_goal_ee3 std_msgs/Bool "data: True" 
    def callback_set_goal_ee3(self, data):
      #p_ee = self.p_ee
      p_ee = list(data.data)
      print("target position")
      print(p_ee)
      #q_ee = self.q_ee
      q_ee_xyzw = self.ee_target_q
      q_ee_wxyz = q_xyzw_to_wxyz(q_ee_xyzw)  # return a list
      q_ee = list_2_quaternion(q_ee_wxyz)
      print("target orientation")
      print(q_ee)
      
      goal_ee3_in_base = array_quat_2_pose(p_ee, q_ee)
      self.goal_pub.publish(goal_ee3_in_base)
# step 1: orientation
# rostopic pub /set_goal_ee3 std_msgs/Float64MultiArray "data: [0.3927942296995117, -0.03321215651462559, 0.3914223987459044]" 
# step 2: hover
# rostopic pub /set_goal_ee3 std_msgs/Float64MultiArray "data: [0.5067963183582014, 0.010948362447869966, 0.3914223987459044]"
# step 3: approach
# rostopic pub /set_goal_ee3 std_msgs/Float64MultiArray "data: [0.5067963183582014, 0.010948362447869966, 0.29]"
# rostopic pub /set_goal_ee3 std_msgs/Float64MultiArray "data: [0.5067963183582014, 0.010948362447869966, 0.19]"
# rostopic pub /set_goal_ee3 std_msgs/Float64MultiArray "data: [0.5067963183582014, 0.010948362447869966, 0.09]"
# rostopic pub /set_goal_ee3 std_msgs/Float64MultiArray "data: [0.5067963183582014, 0.010948362447869966, -0.01]"
# rostopic pub /set_goal_ee3 std_msgs/Float64MultiArray "data: [0.5067963183582014, 0.010948362447869966, -0.095]"


def main(args):
  rospy.init_node("test_grasp", anonymous=True)
  mf = move_franka()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
    
    

