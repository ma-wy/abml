#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *

class franka_rocker_control:
  def __init__(self):
#=======input========================position==========================================================
    self.time_origin_sub = rospy.Subscriber('/time_origin', Float32, self.callback_time_origin)
#    self.rocker_sub = rospy.Subscriber('/external_input', Float64MultiArray, self.callback_rocker)
#    self.target_pose_sub = rospy.Subscriber('/target_pose', PoseArray, self.callback_target)
    self.target_pose_sub = rospy.Subscriber('/target_pose', PoseStamped, self.callback_target)
#=======output==================================================================================

#===============================================================================================
# members
    self.rob = MoveGroupCommander('panda_arm')
    speed = 0.1
    self.rob.set_max_velocity_scaling_factor(speed)
    self.rob.set_max_acceleration_scaling_factor(speed)
#    self.rob.set_joint_position_speed(speed)
    self.rob.set_named_target('ready')
    self.base_frame = 'panda_link0'
    self.ee_frame = 'panda_hand_tcp'
    self.ee_id = self.rob.get_end_effector_link()
#    self.ee_pose = list(self.ee_p) + list(self.ee_q)
    self.target_pose = []

# functions
  def callback_time_origin(self, data):
    t = data
    
  def callback_target(self, data):
#    self.target_pose_list = get_PoseArray(data)
    self.target_pose = get_Pose(data)
    
# class end=========================================================================================
def main(args):
  rospy.init_node('franka_rocker_control', anonymous=True)
  rospy.wait_for_message('move_group/status', GoalStatusArray)
  frc = franka_rocker_control()

  while not rospy.is_shutdown():
#    print(frc.target_pose[0])
    frc.rob.set_pose_target(frc.target_pose, frc.ee_id) #plan
    frc.rob.go() # execute
     
#    for i in range(len(frc.target_pose_list)):
#      frc.target_pose_list[0] -= 0.01
#    print([i[0] for i in frc.target_pose_list])
#    frc.rob.set_pose_targets(frc.target_pose_list, frc.ee_id) #plan
#    frc.rob.go() # execute
#    time.sleep(1)  
  try:
    rospy.spin()

  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)

