#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from franka_utils import *

class rob_move:
  def __init__(self):
#=======input==================================================================================
    self.target_sub = rospy.Subscriber("/ee_target_in_base", PoseStamped, self.callback_rob_target_pose)
    self.target_sub = rospy.Subscriber("/ee_place_target_in_base", PoseStamped, self.callback_rob_place_target_pose)
#=================================================================================
# members

    self.target_pose = []
    self.target_place_pose = []
    
    self.magnet_trigger = Int32()
    self.power_trigger = Int32()
    self.bellow_trigger = Float64()
    self.frame = 'panda_link0'

    print('###################')
    print('ready to move robot')
    print('###################')
    
#===============================================================================================
    
  def callback_rob_target_pose(self, data):
    self.target_pose = data

  def callback_rob_place_target_pose(self, data):
    self.target_place_pose = data

def main(args):
  rospy.init_node('rob_move', anonymous=True)
  rate = rospy.Rate(20)
  rm = rob_move()

  rob = MoveGroupCommander('panda_arm')
  rob.set_end_effector_link('panda_hand_tcp')

  
  
  gripper_grasp_client = actionlib.SimpleActionClient('/franka_gripper/grasp', franka_gripper.msg.GraspAction)
  gripper_grasp_client.wait_for_server()  
  gripper_move_client = actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction)
  gripper_move_client.wait_for_server()      

  rob.go(tempt_pose_init)
  b = franka_open_gripper(client=gripper_move_client, width=0.02, speed=0.1)
  
  while not rospy.is_shutdown():
    fb = rob.get_current_pose()
    print('press enter to check target')
    input()
    pick_pose = deepcopy(rm.target_pose)
    pick_pose_1 = deepcopy(pick_pose)
    pick_pose_2 = deepcopy(pick_pose)
    place_pose = deepcopy(rm.target_place_pose)
    place_pose_1 = deepcopy(place_pose)
    
    print(pick_pose)
    
    pick_pose_1.pose.position.z = fb.pose.position.z
    pick_pose_2.pose.position.z += 0.1
    place_pose_1.pose.position.z += 0.1
    
    print('press enter to move')
    input()
    
    #rob.go(pick_pose_1)
    #rob.go(pick_pose)
    print('magnet')
    print('air pump')
    print('press enter to close gripper')
    #a = franka_close_gripper_black(client = gripper_grasp_client, speed=0.1)
    print(a)
    rob.go(pick_pose_2)  
    
    rob.go(place_pose_1)
    rob.go(place_pose)
    print('magnet')
    print('press enter to open gripper')
    b = franka_open_gripper(client=gripper_move_client, width=0.02, speed=0.1)
    print('air pump')
    rob.go(place_pose_1)
    rob.go(tempt_pose_init)
    

    

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main(sys.argv)

    
    
