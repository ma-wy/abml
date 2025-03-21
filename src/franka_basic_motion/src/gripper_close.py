#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *


def main(args):
  rospy.init_node('test_gripper', anonymous=True)
  
  gripper_grasp_client = actionlib.SimpleActionClient('/franka_gripper/grasp', franka_gripper.msg.GraspAction)
  gripper_grasp_client.wait_for_server()  


  gripper_move_client = actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction)
  gripper_move_client.wait_for_server()  
  
  while True:
    print('close the gripper')
    input()
    a = franka_close_gripper(client = gripper_grasp_client, speed=0.1)
    print(a)
    print('open the gripper')
    input()
    b = franka_open_gripper(client=gripper_move_client, width=0.2, speed=0.1)
    print(b)
    



    
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main(sys.argv)


    
    
    
    
