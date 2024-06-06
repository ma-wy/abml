#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from pose_transform_functions import  array_quat_2_pose, list_2_quaternion, position_2_array, transform_pose


class move_franka():
  def __init__(self):
#input==============================================================================================      
    self.goal_sub = rospy.Subscriber('/camera_goal', Float64MultiArray, self.callback_camera_goal)
    #self.arm_interface = ArmInterface() 
    self.gripper_interface = GripperInterface()
    
   # self.panda_interface = self.arm_interface.get_movegroup_interface() 
    #self.move_group_arm = self.panda_interface.arm_group#MoveGroupCommander('panda_arm')#
    self.move_group_arm = MoveGroupCommander('panda_arm')
    
    self.ee_link = "panda_hand" # The results of panda_hand and panda_link8 are different in orientation, no result of panda_EE
    #self.arm_interface.set_EE_at_frame(self.ee_link)
    self.move_group_arm.set_end_effector_link(self.ee_link)
    self.move_group_arm.clear_pose_targets()
    self.move_group_arm.set_goal_tolerance(0.001)
    
    print("Initialization")
    self.joint_1 = [-0.16962340152681918, -0.4375575387774955, 0.07910295120940916, -2.273439405174825, -0.008065333992826029, 1.596041500063057, 0.710311348411797]
    self.joint_2 = [-0.1688818741207486, -0.4601411580662978, 0.07664149367181877, -2.4933026646743586, -0.00830109743240327, 1.7924220517211489, 0.7097188086215838]
    self.joint_2 = self.move_group_arm.get_current_joint_values()
    self.joint_2[0] = self.joint_1[0]
    self.move_group_arm.go(self.joint_1) # works
    
    pose_1 = self.move_group_arm.get_current_pose().pose
    pose_1.orientation.x = -1#-0.992
    pose_1.orientation.y = 0#0.059
    pose_1.orientation.z = 0#0.11
    pose_1.orientation.w = 0#-0.001
    self.move_group_arm.go(pose_1,wait=True)    
    print(1)
    print(self.move_group_arm.get_current_pose().pose)
    
    pose_1 = self.move_group_arm.get_current_pose().pose
    pose_1.position.x = 0.4004861096556657
    pose_1.position.y = -0.02817132162189055
    pose_1.position.z = 0.3111332983725467
    self.move_group_arm.go(pose_1,wait=True)  
    pose_1 = self.move_group_arm.get_current_pose().pose
    pose_1.orientation.x =-0.9920766835988208
    pose_1.orientation.y =-0.05852491885494221
    pose_1.orientation.z = 0.10979432622930288
    pose_1.orientation.w = 0.0013761033540894904
    self.move_group_arm.go(pose_1,wait=True)      
    print(2)  
    print(self.move_group_arm.get_current_pose().pose)    
    
    '''
    self.move_group_arm.shift_pose_target(5, 1.57, self.ee_link)
    self.move_group_arm.go()    
    print(3)
    print(self.move_group_arm.get_current_pose().pose)   
    '''
    '''
    p_ee = [0.423, 0.002, 0.218]#[0.4004861096556657, -0.02817132162189055, 0.4111332983725467]
    q_ee = [1, 0, 0, 0]
    # [0.707, 0.707, 0, 0] = transformation_Q([1, 0, 0, 0], [0,0,0.707,0.707]) : rot 1. x-axis 180, rot 2. z-axis 90
    print(1)
    print(self.move_group_arm.get_current_pose().pose)
    self.move_group_arm.shift_pose_target(5, 1.57, self.ee_link)
    self.move_group_arm.go()
    print(2)
    print(self.move_group_arm.get_current_pose().pose)
    
    print("before move")
    pose_1 = self.move_group_arm.get_current_pose().pose
    print(pose_1)
    
    pose_1.orientation.x = 0.707#-0.992
    pose_1.orientation.y = 0.707#0.059
    pose_1.orientation.z = 0#0.11
    pose_1.orientation.w = 0#-0.001
    #pose_1.position.x = 0.400
    #pose_1.position.y = -0.028
    #pose_1.position.z = 0.411
    print("target pose")
    print(pose_1)
    #self.move_group_arm.set_orientation_target(q_ee, end_effector_link=self.ee_link)
    self.move_group_arm.set_pose_target(pose_1, end_effector_link=self.ee_link)
    self.move_group_arm.go(pose_1, wait=True)
    print("after move")
    print(self.move_group_arm.get_current_pose().pose)
    '''
    
    
    #q_ee = [1, 0, 0, 0]
    #self.move_group_arm.set_orientation_target(q_ee, end_effector_link=self.ee_link)
    #self.move_group_arm.go(wait=True)
    #self.move_group_arm.set_position_target(p_ee, end_effector_link=self.ee_link)
    #self.move_group_arm.go(wait=True)
     
    print(self.move_group_arm.get_current_joint_values())
    #control joints
    


    
    #This works
    '''
    pose_1 = self.move_group_arm.get_current_pose().pose
    #pose_1.position.z = pose_1.position.z - 0.05
    pose_1.orientation.x = 0#-0.992
    pose_1.orientation.y = 0#0.059
    pose_1.orientation.z = 0.707#0.11
    pose_1.orientation.w = 0.707#-0.001
    # 0 0 0 1 [0.002, 0.002, -0.001]
    # 
    self.move_group_arm.set_pose_target(pose_1, end_effector_link=self.ee_link)
    self.move_group_arm.go(pose_1, wait=True)
    '''
    print("")
    
   # self.move_group_hand = panda_interface.gripper_group
# current ee pose
# rosrun tf tf_echo /panda_link0 /panda_EE

# rosrun tf tf_echo /panda_link0 /camera_color_optical_frame
# or
# rostopic echo /cartesian_pose
# input a target pose of the camera
# don't change the orientation
# data: [x, y, z, qx, qy, qz, qw]
# rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.48, 0.0, 0.60, 0.707, -0.707, 0.0, 0.0]"      
# rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.48, 0.0, 0.40, 0.707, -0.707, 0.0, 0.0]"   
  def callback_camera_goal(self, data):
    print("get goal of camera")
    pose_cam = data.data 
    pose_ee = cam_2_ee_pose(list(pose_cam)) #xyzw
    print(pose_ee)
    p_ee = pose_ee[0:3]
    q_ee = pose_ee[3:7]



    #p_ee = [0.4004861096556657, -0.02817132162189055, 0.4111332983725467]
    #q_ee = [0.9920766835988208, -0.05852491885494221, -0.10979432622930288, 0.0013761033540894904]
    
    
    #self.move_group_arm.set_orientation_target(q_ee, end_effector_link=self.ee_link)
    #self.move_group_arm.go(wait=True)
   # self.move_group_arm.set_position_target(p_ee, end_effector_link=self.ee_link)
   # self.move_group_arm.go(wait=True)
    #q_ee = list_2_quaternion(q_w_trans(pose_ee[3:7]))
    
    pose_target = give_Pose(p_ee,q_ee)
    print("current pose")
    print(self.move_group_arm.get_current_pose().pose)
    print("target pose")
    print(pose_target)
    self.move_group_arm.set_pose_target(pose_target, end_effector_link=self.ee_link)
    self.move_group_arm.go(pose_target, wait=True)
    

    
    #self.move_group_arm.stop()
    #self.move_group_arm.clear_pose_targets()
    '''
current pose
position: 
  x: 0.3724816969156821
  y: -0.035052058725025884
  z: 0.4293829896713139
orientation: 
  x: 0.9922912549592566
  y: -0.012889353432563776
  z: -0.1228478354570088
  w: 0.01001694679040311
target pose
position: 
  x: 0.4004861096556657
  y: -0.02817132162189055
  z: 0.4111332983725467
orientation: 
  x: 0.9920766835988208
  y: -0.05852491885494221
  z: -0.10979432622930288
  w: 0.0013761033540894904
    '''



def main(args):
  rospy.init_node("move_to_camera_goal", anonymous=True)
  mf = move_franka()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
    
    

