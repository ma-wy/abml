#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

class reset_rob(Panda):
    def __init__(self):
#Usage==============================================================================================      
# roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110
# rosrun franka_realsense_calibration reset_rob.py

# run this command to get the joint positions
# rostopic echo /franka_state_controller/joint_states

      self.robot = MoveGroupCommander('panda_arm')
      self.ee_link = "panda_hand" # The results of panda_hand and panda_link8 are different in orientation, no result of panda_EE
      self.robot.set_end_effector_link(self.ee_link)
      self.robot.clear_pose_targets()
      self.robot.set_goal_tolerance(0.001)
    
      print("Initialization")
      print("This pose is good for calibration")
      # camera vertical to the table
      #self.joint = [0.0003840291849296671, -0.2926723564202901, -0.04716859513102915, -2.1602523440908983, -0.03559529406825701, 1.6029944187580367, 0.7608856661899223]
      # revised according to the named target: ready
      self.joint = [0.00020837035262548736, -0.6571359393052546, -0.0002914971227159861, -2.24650358355115, 0.0005913362175536652, 1.4097366510783558, 0.785743671374131]
      self.robot.go(self.joint) 
      
def main(args):
  rospy.init_node("reset_rob", anonymous=True)
  rr = reset_rob()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
    
    

